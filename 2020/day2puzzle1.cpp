
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream infile( "day2puzzle1.txt" );
    string range, character, password;
    int numlines = 0;
    while( infile >> range >> character >> password ) {
        numlines++;
        character = character[0];
        
        cout << range << " " << character << " " << password << endl;
    }
    cout << numlines << " lines" << endl;


}
