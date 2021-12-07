#include <iostream>
#include <regex>
#include <vector>
#include <set>
#include <map>
#include "aoc.h"

using namespace std;
// regex directionRE("(se|sw|ne|nw|e|w)");

typedef map<string, string> Passport;

void addToPassport(const string &line, Passport &pass);
bool process(Passport &pass);

int main(int argc, char **argv) {
  //  Because these guys may be split across multiple lines, we'll parse until
  //  we see an empty line.
  Passport passport;

  int good = 0;
  int bad = 0;
  for (string line; getline(cin, line); ) {
    if (line.size() > 0) {
      addToPassport(line, passport);
    } else if (!passport.empty()) {
      if (process(passport)) {
        ++good;
      } else {
        ++bad;
      }
      passport.clear();
    }
  }
  //  at end of file, we probably have another passport
  if (!passport.empty()) {
    if (process(passport)) {
      ++good;
    } else {
      ++bad;
    }
  }

  cout << "There are " << good << " valid passports!\n";

  return 0;
}

//  here we're going to parse the line and add its
//  elements to passport
void addToPassport(const string &line, Passport &pass) {
  regex pp("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([^ ]+)");

  sregex_iterator ppBegin(line.begin(), line.end(), pp);
  sregex_iterator ppEnd;
  for (sregex_iterator it = ppBegin; it != ppEnd; ++it) {
    string key = it->str(1);
    string val = it->str(2);
    if (key != "cid") {
        pass[key] = val;
    }

//cout << "  Complete match is \"" << it->str() << "\"\n";
//cout << "  I think I found key \"" << key << "\" : \"" << val << "\"\n";
//    cout << "  one match is \"" << pp->str() << "\"\n";
  }
}

//  here we're going to do something with a complete passport
bool process(Passport &pass) {
  if (pass.size() != 7) {
    cout << "  Wrong number of keys: " << pass.size() << " keys\n";
    return false;
  }
  //  here we want to iterate over the keys in the passport
  //for(Passport::iterator it = pass.begin(); it != pass.end(); ++it) {
  for(auto it = pass.begin(); it != pass.end(); ++it) {
    string key = it->first;
    string val = it->second;
//cout << "checking " << key << " value " << val << endl;

//    byr (Birth Year) - four digits; at least 1920 and at most 2002.
//    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
//    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

    if (key == "byr") {
      if (val.size() != 4) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
      int year = stoi(val);
      if ((year < 1920) || (year > 2002)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else if (key == "iyr") {
      if (val.size() != 4) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
      int year = stoi(val);
      if ((year < 2010) or (year > 2020)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else if (key == "eyr") {
      if (val.size() != 4) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
      int year = stoi(val);
      if ((year < 2020) or (year > 2030)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else if (key == "hgt") {
      regex re("^(\\d+)(cm|in)$");
          smatch subs;
          if (!regex_match(val, subs, re, regex_constants::match_default)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
      int height = stoi(subs[1]);
      string units = subs[2];
      if (units == "cm") {
        if ((height < 150) || (height > 193)) {
          cout << "  bad " << key << " " << val << endl;
          return false;
        }
      } else if (units == "in") {
        if ((height < 59) || (height > 76)) {
          cout << "  bad " << key << " " << val << endl;
          return false;
        }
      } else {
        fail("whaa");
      }
      
//    hgt (Height) - a number followed by either cm or in:
//        If cm, the number must be at least 150 and at most 193.
//        If in, the number must be at least 59 and at most 76.
//    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
//    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
//    pid (Passport ID) - a nine-digit number, including leading zeroes.
//    cid (Country ID) - ignored, missing or not.
      
    } else if (key == "hcl") {
      regex re("^#[0-9a-f]{6}$");
      if (!regex_match(val, re)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else if (key == "ecl") {
      regex re("^(amb|blu|brn|gry|grn|hzl|oth)$");
      if (!regex_match(val, re)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else if (key == "pid") {
      regex re("^[0-9]{9}$");
      if (!regex_match(val, re)) {
        cout << "  bad " << key << " " << val << endl;
        return false;
      }
    } else {
      fail("I can't handle \"" + key + "\"");
    }
  }
  return true;
}

