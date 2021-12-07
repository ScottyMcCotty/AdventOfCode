
class Splitter
{
    private:
    int data;
    int length;
    vector<int> split = vector<int>();

    vector<int> splitData(int data);
    vector<int> combineData(int data);
    vector<int> padData(vector<int> data, int length);

    public:
    Splitter(int data);
    Splitter(int data, int length = -1);
    Splitter(vector<int> split);
    Splitter(vector<int> split, int length);

    int data();
    int data(int index);
    vector<int> data();
}

