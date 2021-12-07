#include <iostream>
#include <regex>
#include "aoc.h"


using namespace std;

void split(bool wantHigh, int *min, int *max, int *mid);

// takes a 7 character string consist
int getRow(string bp);

// takes a 3 character string consisting of L and R
int getCol(string bp);

// get ID would split the bp into the 2 substrings
// then call the 2 functions and calculate the ID
int getID(string bp);

// takes the ID, calculates row and col
void getFromID(int ID, int* row, int* col);

int main(int argc, char **argv) {
  
  cout << "getRow(FBFBBFF) should be 44, we calculated " << getRow("FBFBBFF") << endl;
  cout << "getRow(BFFFBBF) should be 70, we calculated " << getRow("BFFFBBF") << endl;
  cout << "getRow(FFFBBBF) should be 14, we calculated " << getRow("FFFBBBF") << endl;
  cout << "getRow(BBFFBBB) should be 103, we calculated " << getRow("BBFFBBB") << endl;
  bool ar[128*8];
  for (int ii = 0; ii < 128 * 8; ++ii) ar[ii] = false;
  for (string line; getline(cin, line); ) {
    int id = getID(line);
    ar[id] = true;
  }
  
  int firstSeat = -1;
  for (int ii = 0; ii < 128 * 8; ++ii) {
    if (ar[ii]) {
      firstSeat = ii;
      break;
    }
  }
  int lastSeat = -1;
  for (int ii = (128 * 8) - 1; ii >= firstSeat; --ii) {
    if (ar[ii]) {
      lastSeat = ii;
      break;
    }
  }
  for (int ii = firstSeat; ii <= lastSeat; ++ii) {
    if (!ar[ii]) {
      cout << "my seat is " << ii << endl;
      cout << "dad is mean" << endl; break;
    }
  }

  // ii = 8 didn't work
  // ii = 10 didn't work
  // ii = 100.
  for(int ii = 0; ii < 128*8; ++ii) {
    cout << ii << " : " << (ar[ii] ? "True":"False") << endl;
  }
    
  int ii = 100;
  while(ar[ii]) {
    ++ii;
  }
  int row, col;
  getFromID(ii, &row, &col);
  cout << "Row is " << row << ", col is " << col << ", and ID is " << ii << endl;
  return 0;
}


int getRow(string bp) {
  int min = 0;
  int max = 127;
  int mid = 128/2;
  
  for(int ii = 0; ii < 7; ++ii) {
    if( bp[ii] == 'F' ) {
      split(false, &min, &max, &mid);
    } else if (bp[ii] == 'B') {
      split(true, &min, &max, &mid);
    } else {
      fail("wtf is bp[" + to_string(ii) + "] " + to_string(bp[ii]) + "!?");
    }
  }
  return mid;
}


int getCol(string bp) {
  int min = 0;
  int max = 7;
  int mid = (min + max + 1) / 2;

  for(int ii = 0; ii < 3; ++ii) {
    if( bp[ii] == 'R' ) {
        split(true, &min, &max, &mid);
    } else if (bp[ii] == 'L') {
        split(false, &min, &max, &mid);
    } else {
      fail("wtf is bp[" + to_string(ii) + "] " + to_string(bp[ii]) + "!?");
    }
  }
  return mid;
}

void split(bool wantHigh, int *min, int *max, int *mid) {
  if (wantHigh) {
    *min = *mid;
  } else {
    *max = (*mid) - 1;
  }
  *mid = ((*min) + (*max) +1) / 2;
}


int getID(string bp) {
    regex re("^([FB]{7})([RL]{3})$");
  smatch subs;
  if (!regex_match(bp, subs, re, regex_constants::match_default)) {
    fail("life is bad, failed to parse boarding pass \"" + bp + "\"");
    return -1;
  }
  int row = getRow(subs[1]);
  int col = getCol(subs[2]);
  int rv = (row * 8) + col;
  cout << "getID(\"" << bp << "\"): row " << row << ", col " << col << ", ID " << rv << endl;
  return rv;
}


void getFromID(int ID, int* row, int* col) {
  *col = ID % 8;
  *row = (ID - *col) / 8;
}





