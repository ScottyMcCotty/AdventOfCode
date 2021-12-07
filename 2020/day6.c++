#include <iostream>
#include <regex>
#include <vector>
#include <set>
#include <map>
#include "aoc.h"

using namespace std;

typedef map<string, int> Answers;

void addQuestions(const string &line, Answers &answers);
int countAnswers(int groupSize, Answers &answers);

int main(int argc, char **argv) {
  //  Because these guys may be split across multiple lines, we'll parse until
  //  we see an empty line.
    Answers answers;
  int sum = 0;
  int groupSize = 0;
  
  for (string line; getline(cin, line); ) {
    if (line.size() > 0) {
      addQuestions(line, answers);
      ++groupSize;
    } else if (!answers.empty()) {
      sum += countAnswers(groupSize, answers);
      answers.clear();
      groupSize = 0;
    }
  }
  //  at end of file, we probably have more answers
  if (!answers.empty()) {
    sum += countAnswers(groupSize, answers);
  }

  cout << "Sum is " << sum << endl;

  return 0;
}

//  here we're going to parse the line and add its
//  elements to passport
void addQuestions(const string &line, Answers &answers) {
  regex pp("[a-z]");

  sregex_iterator ppBegin(line.begin(), line.end(), pp);
  sregex_iterator ppEnd;
  for (sregex_iterator it = ppBegin; it != ppEnd; ++it) {
    string key = it->str();
    //  count() returns the number of elements with the given key... which, in a map,
    //  will be 0 or 1.
    //bool contains = (answers.find(key) == answers.end());
    //int was = (contains) ? answers[key] : 0;
    int was = (answers.count(key) != 0) ? answers[key] : 0;
    answers[key] = was + 1;
  }

//cout << "  Complete match is \"" << it->str() << "\"\n";
//cout << "  I think I found key \"" << key << "\" : \"" << val << "\"\n";
//    cout << "  one match is \"" << pp->str() << "\"\n";
}

int countAnswers(int groupSize, Answers &answers) {
  int count = 0;
  for(auto itr = answers.begin(); itr != answers.end(); ++itr) {
    if(itr->second == groupSize) {
      ++count;
    }
  }
  return count;
}












