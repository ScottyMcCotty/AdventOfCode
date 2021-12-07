
#include <math.h>

Splitter::Splitter(int data)
{
    Splitter(data, -1);
}

Splitter::Splitter(int data, int length)
{
    // save the data
    this->data = data;
    
    // need to split the data
    this->split = this->splitData(data, length);

    // pad the data
    this->padData(this->split, length);
}

Splitter::Splitter(int<vector> split)
{
    Splitter(split, -1);
}

Splitter::Splitter(vector<int> split, int length)
{
    // need to combine the data
    this->data = this->combineData(split);

    // add extra digits if necessary
    this->padData(split, length);

    // save the data
    this->split = split;
}

vector<int> Splitter::splitData(int data, int length)
{
    if (data < 0)
    {
        throw ValueError("Negative numbers confuse me!!");
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
}

vector<int> Splitter::padData(vector<int> &data, int length)
{
    if (length == -1) return;

    if (data.size() > length)
    {
        throw ValueError("More digits given than desired!!");
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
        // bit number is data.size()-1 - ii
        sum += pow(data[ii], data.size()-1 - ii)
    }

    return sum;
}

int Splitter::data()
{
    return this->data;
}

int Splitter::data(int index)
{
    return this->split.at(index);
}

vector<int> Splitter::data()
{
    return this->split;
}