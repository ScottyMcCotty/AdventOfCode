
#include <string>
#include <vector>

using namespace std;

class Splitter
{
    private:
    int data;
    int length;
    vector<int> split = vector<int>();

    vector<int> splitData(int data);
    void padData(vector<int> &data, int length);
    int combineData(vector<int> data);
    
    public:
    Splitter(int data);
    Splitter(int data, int length);
    Splitter(vector<int> split);
    Splitter(vector<int> split, int length);

    int getData();
    int getData(int index);
    vector<int> getSplit();

    string format();
};

