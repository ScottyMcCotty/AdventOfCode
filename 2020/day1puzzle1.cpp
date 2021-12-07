
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ifstream input( "day1puzzle1input.txt" );
    vector<int> values;
    int length = 0;
    string fileline;
    while( input >> fileline ) {
        values.push_back( stoi(fileline) );
        length += 1;
        //cout << stoi( fileline ) << endl;
    }
    
    cout << "Total length: " << length << endl;
    
    for(int ii = 0; ii < length; ii++) {
        for(int jj = ii; jj < length; jj++) {
            for(int kk = jj; kk < length; kk++) {
                if( values[ii] + values[jj] + values[kk] == 2020 ) {
                    cout << "Match found: " << values[ii] * values[jj] * values[kk] << endl;
                }
            }
        }
    }
}
