#include <iostream>
#include <regex>
#include <vector>
#include <set>
#include "aoc.h"

using namespace std;

//  So, because hex grids are the same as square grids with every other row
//  offset half a square, we can store the floor as a 2D array, and every
//  hex gets its own x,y coordinate which lets us find it.  Since we don't
//  know the size of the floor ahead of time (although we could look at the
//  data to figure out the maximum possible size), I propose we call the
//  reference hex 0,0 and grow as needed.  (Although, maybe we don't need
//  to store any tile information other than the relatively small set of
//  coordinates which have been flipped to black.)  Our coordinate scheme
//  might look like this:
//
//
//       [-3, 3]   [-2, 3]   [-1, 3]   [ 0, 3]   [ 1, 3]   [ 2, 3]   [ 3, 3]
//
//
//  [-3, 2]   [-2, 2]   [-1, 2]   [ 0, 2]   [ 1, 2]   [ 2, 2]   [ 3, 2]
//
//
//       [-3, 1]   [-2, 1]   [-1, 1]   [ 0, 1]   [ 1, 1]   [ 2, 1]   [ 3, 1]
//
//
//  [-3, 0]   [-2, 0]   [-1, 0]   [ 0, 0]   [ 1, 0]   [ 2, 0]   [ 3, 0]
//
//
//       [-3,-1]   [-2,-1]   [-1,-1]   [ 0,-1]   [ 1,-1]   [ 2,-1]   [ 3,-1]
//
//
//  [-3,-2]   [-2,-2]   [-1,-2]   [ 0,-2]   [ 1,-2]   [ 2,-2]   [ 3,-2]
//
//
//       [-3,-3]   [-2,-3]   [-1,-3]   [ 0,-3]   [ 1,-3]   [ 2,-3]   [ 3,-3]
//


bool isOdd(int val) {
  return (val % 2) != 0;
}

vector<string> getDirectionsFromLine(const string &line);

class Coordinates {
  public:
  Coordinates();
  Coordinates(int x, int y);
  bool operator<(const Coordinates &that) const;
  string toString() const;
  //private:
  int x, y;
};

class Floor {
  public:
  Floor();
  
  Coordinates directionsToCoordinates(const vector<string> &directions);
  void flipTile(const Coordinates &coords);
  //  So, one way we can go is, have a nextDay() method which returns a new Floor;
  //  but, rather than throwing away a new Floor (and set) instance every day,
  //  how about our nextDay() method *takes* a Floor reference which we begin by
  //  clearing its list of black tiles.  That way, we create two Floor objects, and
  //  flip back & forth between them with every iteration.
    void nextDay(Floor &that) const;
  
  int getNumAdjacent(const Coordinates &coords) const;
  bool isBlack(const Coordinates &coords) const;
  
  int getNumBlackTiles() const;

  void clear();
  void dump() const;
  
  private:
  set<Coordinates> blackTiles;
  Coordinates min;
  Coordinates max;
};

//void check(int x, int y, string directions) {
//  Floor tf;
//  Coordinates tc = tf.directionsToCoordinates(getDirectionsFromLine(directions));
//  if ((x != tc.x) || (y != tc.y)) {
//    fail("for string " + directions + ", expected " + to_string(x) + "," + to_string(y) + ", got " + tc.toString());
//  }
//}

int main(int argc, char **argv) {
  Floor floor;

//  check(0, 1, "ne");
//  check(1, 2, "nene");
//  check(1, 3, "nenene");
//  check(2, 4, "nenenene");

//  check(0, -1, "se");
//  check(1, -2, "sese");
//  check(1, -3, "sesese");
//  check(2, -4, "sesesese");

//  check(-1, 1, "nw");
//  check(-1, 2, "nwnw");
//  check(-2, 3, "nwnwnw");
//  check(-2, 4, "nwnwnwnw");
  
//  check(-1, -1, "sw");
//  check(-1, -2, "swsw");
//  check(-2, -3, "swswsw");
//  check(-2, -4, "swswswsw");
  
//  check(0,0, "sewne");
//  check(0,0, "sesewwnene");
//  check(0,0, "sewsenewne");
//  check(0,0, "sesesewwwnenene");
//  check(0,0, "sewsenewsewnene");
  
  Coordinates tc(0, 0);
  floor.flipTile(tc);
  tc.x = 10;
  floor.flipTile(tc);
  tc.y = 4;
  floor.flipTile(tc);
  if (floor.getNumBlackTiles() != 3) fail("come on man");
  floor.clear();
  
  string line;
  while (getline(cin, line)) {
      vector<string> directions = getDirectionsFromLine(line);
    Coordinates coords = floor.directionsToCoordinates(directions);
    floor.flipTile(coords);
  }
  cout << "There are " << floor.getNumBlackTiles() << " black tiles.\n";

  Floor floor2;
  
  Floor *tf1 = &floor;
  Floor *tf2 = &floor2;
  for (int days = 1; days <= 100; ++days) {
//tf1->dump();
    tf1->nextDay(*tf2);
    if ((days <= 10) || ((days % 10) == 0)) {
      cout << "Day " << days << ": " << tf2->getNumBlackTiles() << endl;
    }
    Floor *tp = tf1;
    tf1 = tf2;
    tf2 = tp;
  }
  
  return 0;
}



vector<string> getDirectionsFromLine(const string &line) {
  vector<string> directions;
  
  regex directionRE("(se|sw|ne|nw|e|w)");
  sregex_iterator dirBegin(line.begin(), line.end(), directionRE);
  sregex_iterator dirEnd;
  for (sregex_iterator it = dirBegin; it != dirEnd; ++it) {
    directions.push_back(it->str());
  }
  
  return directions;
}

Floor::Floor() : min(0, 0), max(0, 0) { }

Coordinates Floor::directionsToCoordinates(const vector<string> &directions) {
  
  // go through the directions vector. Each command will change our current location
  // when we've read the last direction, we are at the final location.
  
//       [-3, 3]   [-2, 3]   [-1, 3]   [ 0, 3]   [ 1, 3]   [ 2, 3]   [ 3, 3]
//
//  [-3, 2]   [-2, 2]   [-1, 2]   [ 0, 2]   [ 1, 2]   [ 2, 2]   [ 3, 2]
//
//       [-3, 1]   [-2, 1]   [-1, 1]   [ 0, 1]   [ 1, 1]   [ 2, 1]   [ 3, 1]
//
//  [-3, 0]   [-2, 0]   [-1, 0]   [ 0, 0]   [ 1, 0]   [ 2, 0]   [ 3, 0]
//
//       [-3,-1]   [-2,-1]   [-1,-1]   [ 0,-1]   [ 1,-1]   [ 2,-1]   [ 3,-1]
//
//  [-3,-2]   [-2,-2]   [-1,-2]   [ 0,-2]   [ 1,-2]   [ 2,-2]   [ 3,-2]
//
//       [-3,-3]   [-2,-3]   [-1,-3]   [ 0,-3]   [ 1,-3]   [ 2,-3]   [ 3,-3]
//
//
//       dx, dy
  // ne: +0, +1  x+1 on odd-numbered rows!
  // e:  +1, +0
  // se: +0, -1  x+1 on odd-numbered rows
  // sw: -1, -1  x-1 on odd-numbered rows
  // w:  -1, +0
  // nw: -1, +1  x-1 on odd-numbered rows
//cout << "directionsToCoordinates()\n";
    int x = 0;
  int y = 0;
  for(int ii = 0; ii < directions.size(); ++ii) {
    bool yIsOdd = (y % 2) != 0;
//cout << "  y == " << y << ", yIsOdd " << yIsOdd << endl;
    string dir = directions[ii];
//cout << "  dir " << ii << " \"" << dir << "\", x " << x << ", y " << y << "\n";
    if (dir == "ne") {
      x += (yIsOdd ? 1 : 0);
      y += 1;
    } else if (dir == "e") {
      x += 1;
    } else if (dir == "se") {
      x += (yIsOdd ? 1 : 0);
//      cout << "WHAT IS Y % 2?? IT'S " << (y % 2 ) << endl;
      y -= 1;
//cout << "    se, now x " << x << ", y " << y << endl;
    } else if (dir == "sw") {
            x -= (yIsOdd ? 0 : 1);
      y -= 1;
    } else if (dir == "w") {
      x -= 1;
    } else if (dir == "nw") {
            x -= (yIsOdd ? 0 : 1);
      y += 1;
    } else {
      fail("unhandled direction " + to_string(ii) + " \"" + directions[ii] + "\"!");
    }
  }
  return Coordinates(x, y);
}


void Floor::flipTile(const Coordinates &coords) {
  if (blackTiles.find(coords) != blackTiles.end()) {
    blackTiles.erase( coords );
  } else {
    blackTiles.insert( coords );
  }
  if (coords.x < min.x) min.x = coords.x;
  if (coords.y < min.y) min.y = coords.y;
  if (coords.x > max.x) max.x = coords.x;
  if (coords.y > max.y) max.y = coords.y;
}

int Floor::getNumBlackTiles() const {
  return blackTiles.size();
}

Coordinates::Coordinates(): x(0), y(0) { }
Coordinates::Coordinates(int arg_x, int arg_y): x(arg_x), y(arg_y) { }

bool Coordinates::operator<(const Coordinates &that) const {
  return (x == that.x) ? y < that.y : x < that.x;
}

string Coordinates::toString() const {
  char buf[80];
  sprintf(buf, "%02d,%02d", x, y);
  return string(buf);
//  return format("{:2},{:2}", x, y);
//  return "[" + to_string(x) + "," + to_string(y) + "]";
}


int Floor::getNumAdjacent(const Coordinates &coords) const {
  // all the black tiles are stored in set blackTiles
  int total = 0;
  int curx = coords.x;
  int cury = coords.y;
  bool yIsOdd = (cury % 2) != 0;
  Coordinates tc;
  // ne:
  tc.x = curx + (yIsOdd ? 1 : 0);
  tc.y = cury + 1;
  if( isBlack(tc) ) ++total;
  
  // e:
  tc.x = curx + 1;
  tc.y = cury;
  if( isBlack(tc) ) ++total;
  
  // se:
  tc.x = curx + (yIsOdd ? 1 : 0);
  tc.y = cury - 1;
  if( isBlack(tc) ) ++total;
  
  // sw:
  tc.x = curx - (yIsOdd ? 0 : 1);
  tc.y = cury - 1;
  if( isBlack(tc) ) ++total;
  
  // w:
  tc.x = curx - 1;
  tc.y = cury;
  if( isBlack(tc) ) ++total;
  
  // nw:
  tc.x = curx - (yIsOdd ? 0 : 1);
  tc.y = cury + 1;
  if( isBlack(tc) ) ++total;
  
  return total;
}

bool Floor::isBlack(const Coordinates &coords) const {
  return blackTiles.find(coords) != blackTiles.end();
}

void Floor::clear() {
    blackTiles.clear();
  min.x = 0;
  min.y = 0;
  max.x = 0;
  max.y = 0;
}
  
void Floor::nextDay(Floor &that) const {
  that.clear();
  Coordinates tc;
  for (tc.x = min.x - 1; tc.x <= max.x + 1; ++tc.x) {
    for (tc.y = min.y - 1; tc.y <= max.y + 1; ++tc.y) {
      int nc = getNumAdjacent(tc);
cout << tc.toString() << " has " << nc << " neighbors\n";
      if (isBlack(tc)) {
          if ((nc == 1) or (nc == 2)) that.flipTile(tc);
        //  otherwise the new copy stays white: "any black tile with
        //  zero or more than two black tiles immediately adjacent to it
        //  is flipped to white."
      } else {
        if (nc == 2) that.flipTile(tc);
      }
    }
  }
}

void Floor::dump() const {
  Coordinates tc;
  for (tc.y = min.y - 1; tc.y <= max.y + 1; ++tc.y) {
    if (isOdd(tc.y)) cout << "     ";
    for (tc.x = min.x - 1; tc.x <= max.x + 1; ++tc.x) {
      if (isBlack(tc)) {
        cout << " X" << tc.toString() << "X ";
      } else {
        cout << "  " << tc.toString() << "  ";
      }
      cout << "  ";
    }
    cout << endl << endl;
  }
  cout << endl;
}








