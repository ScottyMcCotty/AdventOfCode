// aoc.h
#ifndef AOC_H
#define AOC_H

#include <string>

#define fail(a) failAndDie(a, __FILE__, __LINE__)
//  use the "fail()" macro instead.
void failAndDie(std::string msg, const char *filename, int line);

#endif



