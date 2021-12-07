
#include <math.h>
#include "splitter.h"
#include <iostream>

using namespace std;

Splitter::Splitter(int data) : Splitter(data, -1)
{
    // cout << this->data << endl;

    this->length = this->split.size();
}

Splitter::Splitter(int data, int length)
{
    // cout << "Enter constructor:\n\tdata=" << data << "\tlength=" << length << endl;

    // save the data
    this->data = data;
    
    // need to split the data
    this->split = this->splitData(data);

    // pad the data
    this->padData(this->split, length);

    // set the length
    this->length = length;

    // cout << "Exit  constructor:\n\tdata=" << data << "\tlength=" << length << endl;
}

Splitter::Splitter(vector<int> split) : Splitter(split, -1)
{
    // cout << this->data << endl;

    this->length = this->split.size();
}

Splitter::Splitter(vector<int> split, int length)
{
    // need to combine the data
    this->data = this->combineData(split);

    // add extra digits if necessary
    this->padData(split, length);

    // save the data
    this->split = split;

    this->length = length;
}

vector<int> Splitter::splitData(int data)
{
    if (data < 0)
    {
        throw "Negative numbers confuse me!!";
    }

    // There's probably a better way of doing this...
    // 2896 -> [2, 8, 9, 6]
    vector<int> split = vector<int>();

    while (data > 0)
    {
        // get the least significant digit
        int value = data % 10;

        // insert the digit
        split.insert(split.begin(), value);

        // truncate the digit using integer division
        data = data / 10;
    }

    return split;
}

void Splitter::padData(vector<int> &data, int length)
{
    if (length == -1) return;

    if (data.size() > length)
    {
        throw "More digits given than desired!!";
    }

    while (data.size() < length)
    {
        // insert 0's at the front
        data.insert(data.begin(), 0);
    }
}

int Splitter::combineData(vector<int> data)
{
    int sum = 0;

    for (int ii = data.size() - 1; ii >= 0; --ii)
    {
        // value ^ bit number
        sum += pow(data[ii], data.size()-1 - ii);
    }

    return sum;
}

int Splitter::getData()
{
    return this->data;
}

int Splitter::getData(int index)
{
    return this->split.at(index);
}

vector<int> Splitter::getSplit()
{
    return this->split;
}

string Splitter::format()
{
    // not sure the best way to format the data.

    // for now, append each value in the split data onto a string

    string result = "";

    for (int ii = 0; ii < this->split.size(); ++ii)
    {
        result += to_string(this->split.at(ii));

        result += " ";
    }

    return result;
}

Splitter Splitter::operator+(Splitter &other)
{
    // get each splitter's currently split data
    vector<int> shorter = (this->length < other.length) ? this->getSplit() : other.getSplit();
    vector<int> longer  = (this->length < other.length) ? other.getSplit() : this->getSplit();

    // reverse the data so that we can add them more easily
    reverse(shorter.begin(), shorter.end());
    reverse(longer.begin(), longer.end());

    // add the shorter data into the longer data
    for (int ii = 0; ii < shorter.size(); ++ii)
    {
        longer[ii] += shorter[ii];
    }

    // reverse the new data so that it's in the right order
    reverse(longer.begin(), longer.end());

    return Splitter(longer, longer.size());
}

Splitter Splitter::operator*(Splitter &other)
{
    // get each splitter's currently split data
    vector<int> shorter = (this->length < other.length) ? this->getSplit() : other.getSplit();
    vector<int> longer  = (this->length < other.length) ? other.getSplit() : this->getSplit();

    // reverse the data so that we can add them more easily
    reverse(shorter.begin(), shorter.end());
    reverse(longer.begin(), longer.end());

    // add the shorter data into the longer data
    for (int ii = 0; ii < shorter.size(); ++ii)
    {
        longer[ii] *= shorter[ii];
    }

    // reverse the new data so that it's in the right order
    reverse(longer.begin(), longer.end());

    return Splitter(longer, longer.size());
}