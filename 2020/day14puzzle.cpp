


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream infile("day14example.txt");
    string mask;
    // first line of the file is the mask
    getline(infile, mask);
    cout << "Mask: " << mask << endl;
    cout << "Mask: " << mask[5] << endl;
    // all other lines are memory accesses
    string memaccess;
    vector<string> mems;
    while( getline(infile, memaccess)) {
        mems.push_back(memaccess);
    }
    cout << "I have " << mems.size() << " commands to do" << endl;
    for(int ii = 0; ii < mems.size(); ii++ ) {
        cout << mems[ii] << endl;
    }
    
}


