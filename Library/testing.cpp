
#include "splitter.h"
#include <iostream>

using namespace std;

int main()
{
    Splitter s1(1004);
    Splitter s2(1004, 5);

    cout << "s1: " << s1.format() << endl;
    cout << "s2: " << s2.format() << endl;

}