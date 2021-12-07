// aoc.c++
#include <iostream>
#include <stdlib.h>

using namespace std;

void failAndDie(string msg, const char *filename, int line) {
    cerr << filename << " line " << line << ": " << msg << endl;
    exit(1);
}



