#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

#define TOTAL_NUMBER_OF_CUPS 1000000
#define ITERATIONS 10000000

#define fail(a) failAndDie(a, __FILE__, __LINE__)

class Cup {
    public:
    Cup(int val);
    int val;
    Cup *next;
      Cup * nextLowest;
    //  note that these need to bail when next == the first node they started at.
    //  which is going to be "this".  OR when next == NULL, as in our non-circular
    //  list of 3 cups we pull out.
//    bool contains(int value);
    Cup *find(int value);
};



Cup *one;

//  This guy creates the initial list of 9 or whatever cups, and also sets
//  the global "one" pointer.  In the returned list, the last element will
//  point back to the first.
Cup * createCups(vector<int> cups);

vector<int> getStartingCups(int starting);

void dump(Cup *cups, bool verbose = false);

//  This guy takes the current cup, fiddles the list, and returns the new current cup.
Cup *run(Cup *current);

//  use the "fail()" macro instead.
void failAndDie(string msg, const char *filename, int line);



int main(int argc, char **argv) {

  //  We either want two versions, one commented out, with the example input and
  //  our real input, or we want to pass a flag saying which to use or something.

  //  this is the example list: 389125467
  //  this was my real puzzle input: 318946572
    // mine: 789465123
  vector<int> sample{3,1,8,9,4,6,5,7,2};
  Cup *cup = createCups( sample );
  //dump(cup, true);
  
  for (int ii = 0; ii < ITERATIONS; ++ii) {
    //if ((ii % 1000) == 0) cout << "iteration " << ii << endl;
    cup = run(cup);
  }
  //  now we want the two elements after one.
  //dump(cup);
  int val1 = one->next->val;
  int val2 = one->next->next->val;
  cout << "If this were part 2, the answer would be " << val1 << " * " << val2 << " = " << (long(val1)*long(val2)) << endl;
  
  return 0;
}

Cup::Cup(int val) : val(val), next(nullptr) { }

Cup * Cup::find(int value) {
  if( val == value ) {
    return this;
  }
  Cup * nextCup = next;
  while(( nextCup != nullptr) and (nextCup != this )) {
    if( nextCup->val == value ) {
      return nextCup;
    }
    nextCup = nextCup->next;
  }
  return nullptr;
}

void failAndDie(string msg, const char *filename, int line) {
  cerr << filename << " line " << line << ": " << msg << endl;
  exit(1);
}


Cup * createCups(vector<int> cups) {
  
  // create the first cup from the first element of the vector, and save the first cup twice
  Cup * firstCup = new Cup(cups[0]);
  Cup * someOtherCup = firstCup;
  if( cups[0] == 1 ) {
    one = firstCup;
  }
  
  // make a cup from each of the values in the incoming cups vector
  for(int ii = 1; ii < cups.size(); ii++) {
    Cup * currentCup = new Cup(cups[ii]);
    if( cups[ii] == 1 ) {
      one = currentCup;
    }
    someOtherCup->next = currentCup;
    someOtherCup = currentCup;
  }

  //  this is pretty painless because there are only 9 of them
  one = firstCup->find(1);
  
  for (int ii = 2; ii <= 9; ++ii) {
    firstCup->find(ii)->nextLowest = firstCup->find(ii - 1);
  }
  
  
  // now add in the rest of the cups labeled 10 to max
  int ii = 11;
  someOtherCup->next = new Cup(10);
  someOtherCup->next->nextLowest = firstCup->find(9);
  someOtherCup = someOtherCup->next;
  
  while( ii <= TOTAL_NUMBER_OF_CUPS ) {
    Cup * currentCup = new Cup(ii);
    someOtherCup->next = currentCup;
    currentCup->nextLowest = someOtherCup;
    someOtherCup = currentCup;
    ii++; // almost forgot this line
  }
  
  // now make it circular
  someOtherCup->next = firstCup;
  
  // set cup one's nextlowest
  one->nextLowest = someOtherCup;
  
  // aaaand return the first cup
  return firstCup;
}

void dump(Cup *cups, bool verbose) {
  Cup * nextCup = cups->next;

  /*
  cout << cups->val;
  if (verbose) {
    cout << ", next is " ...
  }
  */
  
  if(verbose) {
      cout << cups->val << ", next is " << ((cups->next != nullptr)?to_string(cups->next->val):"null")
      << ", next lowest is " << cups->nextLowest->val;
  } else {
    cout << cups->val;
  }
  while( (nextCup != cups) and (nextCup != nullptr) ) {
    if(verbose) {
      cout << endl << nextCup->val << ", next is " << ((nextCup->next != nullptr)?to_string(nextCup->next->val):"null")
        << ", next lowest is " << nextCup->nextLowest->val;
    } else {
        cout << " " << nextCup->val;
    }
    nextCup = nextCup->next;
  }
  cout << endl;
  
}
  

//  Remove the three elements after the current cup;
//
Cup *run(Cup *current) {
  // remove the next 3 cups from the list
  // the current cup next should point to the first cup which was after the removed cups (a.k.a. it would have been current->next->next->next->next)
  // find the "destination" cup
  //   make sure the destination isn't in our list of pulled cups
  //   (and that's a loop... "while the destination is in the pulled cups,
  //   subtract one; if we get to zero, wrap around...")
  // insert the removed cups after the destination cup
  // the new current cup is whatever cup comes after our current cup
  

  //  pull the 3 cups after the current cup
  //  pick a destination cup
  //    while it's in the list of pulled cups, pick a new one
  //  insert the pulled cups after the destination cup
  //  return the cup after the current cup
  
  Cup * pulledCups = current->next;
  current->next = pulledCups->next->next->next;
  pulledCups->next->next->next = nullptr;
  //  That's it!  We've removed those three cups from the list!

  
  Cup * destination = current->nextLowest;
  //  if dest == 0...
  //  while (dest is in pulled cups)
  //    --dest
  //    if (dest == 0) ...
  while( pulledCups->find(destination->val) != nullptr ) {
    destination = destination->nextLowest;
  }
  
  pulledCups->next->next->next = destination->next;
  destination->next = pulledCups;
  
  return current->next;
}










  

