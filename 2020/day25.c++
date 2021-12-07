#include <iostream>
#include "aoc.h"

using namespace std;



int countLoops(int subject, int want);

//  This returns the new initial value if you were to continue this
//  transformation mid-way through the total desired number of loops.
//  This comment didn't make sense to me even *as* I was writing it.
int getResult(int initialValue, int subject, int loops);

int main(int argc, char **argv) {

  int cardSubject = 7;
  int cardKey = 5764801;
  int doorSubject = 7;
  int doorKey = 17807724;
    
  // for scott's input:
   cardKey = 16616892;
   doorKey = 14505727;

  //  for Dad's input:
  // cardKey = 5290733;
  // doorKey = 15231938;
  
  // loops number is the smallest number s.t. (x *= 7) % 20201227   loop number of times
  int cardLoops = countLoops(cardSubject, cardKey);
  cout << "Card loop size is " << cardLoops << endl;
  int doorLoops = countLoops(doorSubject, doorKey);
  cout << "Door loop size is " << doorLoops << endl;

  int encryptionKey;
  if (cardLoops < doorLoops) {
    encryptionKey = getResult(1, doorKey, cardLoops);
  } else {
    encryptionKey = getResult(1, cardKey, doorLoops);
  }
  cout << "encryption key is " << encryptionKey << endl;
  
  //  We want a function which takes a subject number and a result, and
  //  performs the transformation repeatedly until it gets the result,
  //  and returns the loop count.  (Using the example, if we call that
  //  with a subject number of 7 and a result of 5764801, the card's
  //  public key, that should give us a loop size of 8.  Calling it again
  //  with a subject number of 7 and a result of 17807724, the door's
  //  public key, should give us 11.)
  //
  //  We also want a function which takes a subject number and a loop
  //  count, and gives us the result.  Then, whichever loop size is
  //  smaller, we use that, and the other device's public key, to get the
  //  encryption key.
  //
  //  Actually, that first function could call the second function
  //  repeatedly with a loop count of 1, but maybe that's silly; we
  //  couldn't possibly screw up the transformation by writing it twice,
  //  unless I'm the one writing one of them.

  return 0;
}


int getResult(int initialValue, int subject, int loops) {
  // largest possible number is 20201226 * subject
  // max int is 2 billion-ish
  long result = initialValue;
  for(int ii = 0; ii < loops; ++ii) {
    result *= (long)subject;
    if (result < 0) fail("oops, Scott was right; long long");
    result = result % 20201227;
  }
  //  if this guy > INT_MAX or whatever before this step, we fail silently here
  //if( (int)result < 0 ) fail("About to return a negative result...");
  return (int)result;
}

int countLoops(int subject, int want) {
  int rv = 0;
  int got = 1;
  while (got != want) {
    ++rv;
    got = getResult(got, subject, 1);
    if((rv % 100000) == 0) cout << "Subject is " << subject << " after loop " << rv << endl;
  }
  return rv;
}

