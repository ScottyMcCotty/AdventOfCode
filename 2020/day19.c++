#include <iostream>
#include <regex>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include "aoc.h"

using namespace std;

struct Rule {
  Rule() : id(-1), literal('\0') { }

  int id;
  //  "and" these rules, "or" these rules, and just-matches-this-string
  char literal;
  vector<int> andOps;  //  only looked at if literal is \0
  vector<int> orOps;  //  only looked at if literal is \0

  bool matches(const string &str, int &pos) const;
};
//ostream &operator<<(ostream &os, const Rule &rule);


void parseRule(const string &line);

void updateRules();

static vector<Rule> rules;

// day 19
int main(int argc, char** argv) {

  //  first, parsing our rules
  for(string line; getline(cin, line); ) {
    if (line.size() == 0) {
      break;
    }
    parseRule(line);
  }
  
  // updateRules
  updateRules();

  //  now, parsing our messages
  int matches = 0;
  for(string line; getline(cin, line); ) {
    int pos = 0;
    if (rules[0].matches(line, pos) && (pos == line.size())) {
      cout << "match: " << line << endl;
      ++matches;
    } else {
      cout << "NO:    " << line << endl;
    }
  }
  cout << matches << " matches!\n";
  return 0;
}

//  Returns true if this rule matches exactly the characters at the given pos,
//  and updates pos to the index after this one.  So, if our rule is
//    666: 4 1 5
//  because literal = \0
//  then first we're going to start at pos 0, and ask rule 4 whether it matches.
//  if it does, then it will have updated pos to the first character AFTER what
//  it matched, and we're going to ask rule 1 whether the characters AT THAT POS
//  match.  If it does, then it will have updated pos to the first character AFTER
//  what it matched, and we're going to ask rule 5 whether the characters AT THAT POS
//  match.
static string indent;
static const int indentAmount = 1;

bool Rule::matches(const string &str, int &pos) const {
  bool blather = true;//(id == 8) || (id == 11);
  if (blather) {
    cout << indent << "rule " << id << ": " << str << endl;
    string pad(to_string(id).size(), ' ');
    cout << indent << "     " << pad << "  ";
    for (int ii = 0; ii < pos; ++ii) cout << " ";
    cout << "^ " << pos << endl;
    indent.resize(indent.size() + indentAmount, ' ');
  }
  if (literal != '\0') {
    if (blather) {
      bool rv = (str[pos] == literal);
      cout << indent << (rv ? "passed" : "failed") << " \"" << literal << "\" rule, returning " << (rv ? "true" : "false") << "!\n";
      indent.resize(indent.size() - indentAmount);
    }
    return (str[pos++] == literal);
  }
  //  Take this rule:
  //  1: 2 3 | 3 2
  //  andOps = 2, 3
  //  orOps = 3, 2
  //
  //    say rule 2 is "a" and rule 3 "b"
  //    str = "snarfbaflab" and pos == 5
  //    we're going to call rule 2 with pos = 5; it's going to return false.
  //
  //  we're going to run through andOps.  IF any of them fail,
  //  else check and/or
  int subpos = pos;
  bool happy = true;
  for(int ii = 0; ii < andOps.size(); ii++) {
    if (!rules[andOps[ii]].matches(str, subpos)) {
      if (blather) {
        cout << indent << "failed to match \"and\" rule " << andOps.at(ii) << "...\n";
      }
      happy = false;
      break;
    }
    if (blather) {
      cout << indent << "passed \"and\" rule " << andOps.at(ii) << "...\n";
    }
  }
  //  If we got here, and we're happy, then return true
  if (happy) {
      pos = subpos;
    if (blather) {
      cout << indent << "passed \"and\" rules, returning true!\n";
      indent.resize(indent.size() - indentAmount);
    }
    return true;
  }
  
  if (orOps.size() == 0) {
    if (blather) {
      cout << indent << "failed \"and\" rules, no \"or\" rules, returning false!\n";
      indent.resize(indent.size() - indentAmount);
    }
    return false;  //  we don't have any or ops!
  }

  for(int ii = 0; ii < orOps.size(); ii++) {
    if (!rules[orOps[ii]].matches(str, pos)) {
      if (blather) {
        cout << indent << "failed to match \"or\" rule " << orOps[ii] << ", returning false\n";
        indent.resize(indent.size() - indentAmount);
      }
      return false;
    }
    if (blather) {
      cout << indent << "passed \"or\" rule " << orOps[ii] << "...\n";
    }
  }
  if (blather) {
    cout << indent << "passed \"or\" rules, returning true!\n";
    indent.resize(indent.size() - indentAmount);
  }
  return true;
}

void parseRule(const string &line) {
  //regex ruleLine("^(\\d+):( (\\d+|\"[a-z]\"|\\|))+$");
  regex ruleLine("^(\\d+): (.+)$");
  regex rulebit("(\\d+|\"[a-z]\"|\\|)");
  
  smatch subs;
  if (!regex_match(line, subs, ruleLine)) {
    fail("bad rule line: \"" + line + "\"");
  }
  int id = stoi(subs[1]);
cout << "rules line \"" << line << "\", got id " << id << endl;
  //  need to ensure the capacity of the rules vector; make sure rules[id] is a real thing
  while (rules.size() <= id) rules.push_back(Rule());
  rules.at(id).id = id;
  string bits = subs[2];
cout << "  sub bits are \"" << bits << "\"\n";

  bool isOr = false;
  sregex_iterator bitsBegin(bits.begin(), bits.end(), rulebit);
  sregex_iterator end;
  for (sregex_iterator it = bitsBegin; it != end; ++it) {
cout << "    \"" << it->str() << "\"\n";
    if (it->str() == "|") {
      isOr = true;
    } else if (it->str()[0] == '"') {
      rules.at(id).literal = it->str()[1];
    } else {
      //  it's a rule ID
      int otherRule = stoi(it->str());
      if (isOr) rules.at(id).orOps.push_back(otherRule);
      else rules.at(id).andOps.push_back(otherRule);
    }
  }
}

void updateRules() {
//  rules.at(8).andOps.clear();
//  rules.at(8).andOps.push_back(42);
//  rules.at(8).orOps.clear();
  rules.at(8).orOps.push_back(42);
  rules.at(8).orOps.push_back(8);

//  rules.at(11).andOps.clear();
//  rules.at(11).andOps.push_back(42);
//  rules.at(11).andOps.push_back(31);
//  rules.at(11).orOps.clear();
  rules.at(11).orOps.push_back(42);
  rules.at(11).orOps.push_back(11);
  rules.at(11).orOps.push_back(31);
}

/*
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
*/

/*
ostream &operator<<(ostream &os, const Rule &rule) {
  if (literal != '\0') {
    os << "\"" << literal << "\"";
  } else {
    for (int ii = 0; ii < andOps.size(); ++ii) {
    }
  }
}
*/

// 199 too low :(

