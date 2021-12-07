
#include "splitter.h"
#include <iostream>

using namespace std;

int main()
{
    cout << endl;


    cout << "From a number:" << endl;

    Splitter s1(1004);
    Splitter s2(1004, 5);
    cout << "  s1: " << s1.format() << endl;
    cout << "  s2: " << s2.format() << endl;

    cout << "From a list of numbers:" << endl;

    Splitter s3({1,2,3,4});
    Splitter s4({1,2,3,8}, 6);
    cout << "  s3: " << s3.format() << endl;
    cout << "  s4: " << s4.format() << endl;

    cout << "Addition:" << endl;

    Splitter s5 = s1 + s2;
    Splitter s6 = s3 + s4;
    cout << "  s5: " << s5.format() << endl;
    cout << "  s6: " << s6.format() << endl;

    cout << "Multiplication:" << endl;

    Splitter s7 = s1 * s2;
    Splitter s8 = s3 * s4;
    cout << "  s7: " << s7.format() << endl;
    cout << "  s8: " << s8.format() << endl;


    cout << endl;
}