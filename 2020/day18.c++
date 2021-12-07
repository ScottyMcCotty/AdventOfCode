#include <iostream>
#include <regex>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include "aoc.h"

using namespace std;

struct Expression {
  Expression(string token) : token(token), lhs(nullptr), rhs(nullptr) { }

  //  when you do this:
  //  Expression *someFunction() {
  //    Expression foo;
  //    ...
  //    return &foo;  //  LOOK OUT
  //  }
/*
example input:
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2

start of processTokens():
  1 + 2 * 3 + 4 * 5 + 6
after +:
  [1 + 2] * 3 + 4 * 5 + 6
after +:
  [1 + 2] * [3 + 4] * 5 + 6
after +:
  [1 + 2] * [3 + 4] * [5 + 6]
after *:
  [[1 + 2] * [3 + 4]] * [5 + 6]
after *:
  [[[1 + 2] * [3 + 4]] * [5 + 6]]


*/

  string token;
  Expression *lhs;
  Expression *rhs;
  
  long evaluate();
};
ostream &operator<<(ostream &os, const Expression &expr);

vector<Expression *> getTokens(const string &line);
void dump(const string &message, vector<Expression *> &tokens);

Expression *processTokens(vector<Expression *> &tokens);

void findPPair(vector<string> tokens, int* first, int* second);
void simplifyTokens(vector<string> *tokens);

int main(int argc, char** argv) {
  
  long sum = 0;
  
  for(string line; getline(cin, line); ) {
    vector<Expression *> tokens = getTokens(line);
    Expression *te = processTokens(tokens);
    sum += te->evaluate();
    //  here we are leaking the entire tree
  }
  
  cout << "Sum: " << sum << endl;
}



vector<Expression *> getTokens(const string &line) {
  regex re("(\\d+|\\+|\\*|\\(|\\))");

  vector<Expression *> rv;
  sregex_iterator reBegin(line.begin(), line.end(), re);
  sregex_iterator reEnd;
  for (sregex_iterator it = reBegin; it != reEnd; ++it) {
    rv.push_back(new Expression(it->str()));
  }
  return rv;
}

Expression* processTokens(vector<Expression *> &tokens) {
  //  first, build the expression tree
  //  second, return the result of evaluating the expression tree
  Expression *curr = nullptr;

dump("start of processTokens()", tokens);
  
  //  first, coalesce parentheses
  stack<int> pstack;
  for (int ii = 0; ii < tokens.size(); ++ii) {
    Expression *te = tokens[ii];
    if (te->token == "(") {
      pstack.push(ii+1);
    } else if (te->token == ")") {
      int first = pstack.top();
      pstack.pop();

      vector<Expression *> subv(tokens.begin() + first, tokens.begin() + ii);
      Expression *sub = processTokens(subv);
      //  leaking both parentheses Expressions here
      //delete tokens[ii + 1];
      tokens.erase(tokens.begin() + first, tokens.begin() + ii + 1);
      //delete tokens[first - 1];
      tokens[first - 1] = sub;
      ii = first - 1;
dump("after closing parenthesis", tokens);
    }
  }

  //  now +
  for (int ii = 0; ii < tokens.size(); ++ii) {
    if ((tokens[ii]->token == "+") && (tokens[ii]->lhs == nullptr)) {
      tokens[ii]->lhs = tokens[ii - 1];
      tokens[ii]->rhs = tokens[ii + 1];
      tokens.erase(tokens.begin() + ii + 1);
      tokens.erase(tokens.begin() + ii - 1);
      --ii;
dump("after +", tokens);
    }
  }

  //  now *
  for (int ii = 0; ii < tokens.size(); ++ii) {
    if ((tokens[ii]->token == "*") && (tokens[ii]->lhs == nullptr)) {
      tokens[ii]->lhs = tokens[ii - 1];
      tokens[ii]->rhs = tokens[ii + 1];
      tokens.erase(tokens.begin() + ii + 1);
      tokens.erase(tokens.begin() + ii - 1);
      --ii;
dump("after *", tokens);
    }
  }

  if (tokens.size() != 1) {
    fail("after processing, " + to_string(tokens.size()) + " tokens");
  }
  return tokens[0];
  
  // while size of tokens > 1
  // find an additon sign and do addition of the stuff on either side
  //.      if one of those things is ( or ), don't do that addition yet
  //
  //  ( 1 * 2 ) + ( 3 * 4 ) + 5
  //  2 + ( 3 * 4 ) + 5
  //  2 + 12 + 5
  
  //    1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) ) still becomes 51.
  //    1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )
  //    1 + 6 + ( 4 * 11 )
  //    7 + ( 4 * 11 )
  //    7 + 44

  //    2 * 3 + (4 * 5) becomes 46.
  //    2 * 3 + ( 4 * 5 )
  //    2 * 3 + 20
  //    2 * 23

  //    5 + ( 8 * 3 + 9 + 3 * 4 * 3 ) becomes 1445.
  //    5 + ( 8 * 12 + 3 * 4 * 3 )
  //    5 + ( 8 * 15 * 4 * 3 )
  //    5 + ( 8 * 15 * 4 * 3 )



  
  //    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
  //    5 * 9 * ( 7 * 3 * 3 + 9 * 3 + ( 8 + 6 * 4 ) )  start
  //    5 * 9 * ( 7 * 3 * 12 * 3 + ( 8 + 6 * 4 ) )         addition
  //    5 * 9 * ( 7 * 3 * 12 * 3 + ( 14 * 4 ) )        addition
  //    45 * ( 7 * 3 * 12 * 3 + ( 14 * 4 ) )           mul
  //    45 * ( 21 * 12 * 3 + ( 14 * 4 ) )              mul
  //    45 * ( 252 * 3 + ( 14 * 4 ) )                  mul
  //    45 * ( 756 + ( 14 * 4 ) )
  //    45 * ( 756 + 56 )
  //    45 * 812

  //    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

  //  (( 1 * 2 ) + 3 ) + ( 3 + 4 )
  //  (( 1 * 2 ) + 3 ) + 7
  //  (( 1 * 2 ) + 3 ) + 7

#if 0
  for (int ii = 0; ii < tokens.size(); ++ii) {
    string token = tokens[ii].token;
//    if (token == "(") {
//      ss.push(curr);
//      curr = nullptr;
//    } else if (token == ")") {
//      Expression *tos = ss.pop();
//      if (tos == nullptr) {
//        //  this was an expression starting with (
//      } else {
//        tos->
//      }
//    } else
    if ((token == "+") || (token == "*")) {
      
    } else if ((token.size() == 1) && isdigit(token[0)) {
      
    } else {
      fail("failed to handle token \"" + token + "\"");
    }
  }
#endif
}

long Expression::evaluate() {
  if ((lhs == nullptr) or (rhs == nullptr)) {
    return stol(token);
  } else if (token == "+") {
    return lhs->evaluate() + rhs->evaluate();
  } else if (token == "*") {
    return lhs->evaluate() * rhs->evaluate();
  } else {
    fail("Unknown expression: \"" + token + "\"");
    return -1;
  }
}
                                                    
#if 0
void simplifyTokens(vector<string> tokens) {
  int first = -1;
  int second = -1;
  findPPair(tokens, &first, &second);
  if (first != -1) {
    // a pair of parantheses were found
    // break into 2 or 3 token sub-vectors
    if ((second == (tokens.size()-1)) and (first == 0)) {
      // the parentheses are on both ends, so we just simplify the middle
      auto firstStart = tokens.start();
      auto firstEnd = tokens.start() + first -2;
      auto secondStart = tokens.start()
      vector<string> subtokens =
    }
  }
}

void findPPair(vector<string> tokens, int* first, int* second) {
  int additionalFound = 0;
  bool firstFound = false;
  
  for(int ii = 0; ii < tokens.size(); ii++) {
    if((tokens[ii] == "(") and (not firstFound)) {
      if (not firstFound) {
        *first = ii;
        firstFound = true;
      } else {
        ++additionalFound;
      }
    } else if (tokens[ii] == ")") {
      if (additionalFound == 0) {
        *second = ii;
        return;
    } else {
        --additionalFound;
      }
    }
  }
  
  if (first != -1) {
    fail("Unbalanced paranthesiessis in findPPair");
  }
  return;
}
#endif

ostream &operator<<(ostream &os, const Expression &expr) {
  if (expr.lhs != nullptr) {
    os << "[" << *(expr.lhs) << " ";
  }
  os << expr.token;
  if (expr.rhs != nullptr) {
    os << " " << *(expr.rhs) << "]";
  }
  return os;
}

void dump(const string &message, vector<Expression *> &tokens) {
  cout << message << ":\n ";
  for (int ii = 0; ii < tokens.size(); ++ii) {
    cout << " " << *(tokens[ii]);
  }
  cout << endl;
}

