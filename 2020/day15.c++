
#include <string>
#include <istream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
    
    
//    vector<string> lines;
//    for (string line; getline(cin, line); ) {
//        cout << "read \"" << line << "\"\n";
//        lines.push_back( line );
//    }
//
//
    
    const int FINALTURN = 30000000;
    
    
    std::vector<int> starting{5,2,8,16,18,0,1};
    int turn = 2;
    std::vector<vector<int>> spoken;
    for(int ii = 0; ii < starting.size(); ii++ ) {
        vector<int> current{starting[ii], turn};
        spoken.push_back(current);
        turn++;
    }
    
    int currentNum = 0;
    
    while( turn <= FINALTURN ) {
        bool found = false;
        int index;
        for(int ii = spoken.size()-1; ii >= 0; ii--) {
            if( currentNum == spoken[ii][0] ) {
                found = true;
                index = ii;
                break;
            }
        }
        if( found ) {
            int tmp = turn - spoken[index][1];
            vector<int> current{currentNum, turn};
            spoken.push_back(current);
            currentNum = tmp;
        } else {
            vector<int> current{currentNum, turn};
            spoken.push_back(current);
            currentNum = 0;
        }
        turn++;
    }
    
    //for(int ii = 0; ii < spoken.size(); ii++ ) {
    //    cout << spoken[ii][0] << " : " << spoken[ii][1] << endl;
    //}
    cout << currentNum << endl;
    return 0;
}
