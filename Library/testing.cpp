
#include "splitter.h"
#include <iostream>

using namespace std;

int main()
{
    cout << endl;


    Splitter s1(1004);
    Splitter s2(1004, 5);

    cout << "s1: " << s1.format() << endl;
    cout << "s2: " << s2.format() << endl;

    Splitter s3({1,2,3,4});
    Splitter s4({1,2,3,4}, 6);

    cout << "s3: " << s3.format() << endl;
    cout << "s4: " << s4.format() << endl;




    cout << endl;
}