

#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

// Function to return GCD of two numbers
// not called directly. Used by LCM function
long long gcd(long long int a, long long int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
 
// Function to return LCM of two numbers
long long lcm(int a, int b) {
    if( a < 0 or b < 0 ) {
        cout << "Negative inputs spotted!" << endl;
    }
    long long ret = (a / gcd(a, b)) * b;
    if( ret < 0 ) {
        cout << "My LCM is negative for some reason. I was passed\na = " << a << "\nb = " << b << "\nand think the LCM(a,b) is " << ret << endl;
    }
    return ret;
}

int main() {
//    // make ifstream object
//    ifstream infile("day13example.txt");
//    string line;
//
//    // dump first line of file
//    infile >> line;
//    // get second line of fine
//    infile >> line;
//    infile.close();
    
    // ah forget it,
    // i'm just going to hardcode the vector of numbers and offsets
    
    // for solving example:
//    std::vector<int> nums{ 7,13,59,31,19 };
//    std::vector<int> offsets{ 0,1,4,6,7 };
//    int maxBus = 59;
//    int maxBusOffset = 4;
    
    // for solving problem:
    std::vector<long long> nums{ 23,41,647,13,19,29,557,37,17 };
    std::vector<long long> offsets{ 0,13,23,41,42,52,54,60,71 };
    long long maxBus = 647;
    long long maxBusOffset = 23;
    
    // for doing other example tests:
//    std::vector<int> nums{ 1789,37,47,1889 };
//    std::vector<int> offsets{ 0,1,2,3 };
//    int maxBus = 19;
//    int maxBusOffset = 3;
    
    clock_t start, end;
    start = clock();
    
    // start with first number
    long long testtime = nums[0];
    long long increment = nums[0];
    
    // increase testtime by increment until testtime is
    for(int ii = 1; ii < nums.size(); ii++) {
        while( ((testtime + offsets[ii]) % nums[ii]) != 0 ) {
            testtime += increment;
        }
        increment = lcm( increment, nums[ii] );
        cout << "Increment is now: " << increment << endl;
    }
    
    end = clock();
    cout << "Solution: " << testtime << endl;
    cout << "Time taken: " << double(end-start) / double(CLOCKS_PER_SEC) << endl;
    return 0;
    
    
    // 527809393542 is too low
    
    //long long testtime = 0;
    bool foundIt = false;
    while( not foundIt ) {
        testtime += maxBus;
        
        bool findingIt = true;
        for( int ii = 0; ii < nums.size(); ii++ ) {
            long long tmp = testtime - maxBusOffset + offsets[ii];
            if( tmp % nums[ii] != 0 ) {
                findingIt = false;
                break;
            }
        }
        
        foundIt = findingIt;
    }
    
    end = clock();
    
    testtime -= maxBusOffset;
    cout << "Time: " << testtime << endl;
    cout << "Time taken: " << double(end - start) / double(CLOCKS_PER_SEC) << endl;
    

}

