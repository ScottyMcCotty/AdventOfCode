
import copy

global size

class CupList:
    def __init__(self, data):
        self.data = data

    def get(self, ii):
        return self.data[ii % len(self.data)]

    def getSubList(self, ii):
        return [self.get(ii+1), self.get(ii+2), self.get(ii+3)]

    # sets a single value
    def set(self, ii, value):
        self.data[ii % len(self.data)] = value
        return

    # takes a sublist and puts the values into the data
    def setSubList(self, ii, values):
        for value in values:
            self.set(ii, value)
            ii += 1
        return

    # prints all the cups
    def printAll(self):
        print("cups: ",end='')
        for value in self.data:
            print(value,end=' ')
        print()

    # returns size of the list
    def size(self):
        return len(self.data)

    # returns the index of the given cup
    def find(self, value):
        return self.data.index(value)

    # returns the value of the destination cup
    def getDestination(self, curCup, extracted):
        lookingFor = curCup-1
        while lookingFor > 0:
            if lookingFor not in extracted:
                return lookingFor
                return self.find(lookingFor)
            else:
                lookingFor -= 1
        lookingFor = 1000000
        lookingFor = max(self.data)
        while True:
            if lookingFor not in extracted:
                return lookingFor
                return self.find(lookingFor)
            else:
                lookingFor -= 1
        print("YOU SHOULD NEVER SEE THIS")
        return

    def finish(self):
        ind = self.find(1)
        print("Answers:")
        print(self.get(ind+1))
        print(self.get(ind+2))

class Chunk:
    def __init__(self, values, start, end):
        self.values = values
        self.start = start
        self.end = end

    def add(self, otherChunk):
        if self.start == otherChunk.end+1:
            # otherChunk goes first
            return Chunk( otherChunk.values + self.values, otherChunk.start, self.end)
        elif self.end+1 == otherChunk.start:
            # this chunk goes first
            return Chunk( self.values + otherChunk.values, self.start, otherChunk.end)
        else:
            print("Chunk",self.start,self.end,"and Chunk",otherChunk.start,otherChunk.end,\
                  "don't go together. Something went wrong")

    def split(self, value):
        # find the value in this chunk, and split
        # first chunk is up to and including value.
        # second chunk is the remaining parts
        if value in self.values:
            spot = self.values.index(value)
        else:
            print("Chunk",self.start,self.end,"does not have value",value)
            

def getNext(data, current):
    curIndex = data.index(current)
    extracted = getExtracted(data, curIndex)
    print(curIndex)



f = open("day23example.txt")


data = ["789465123"]

# for example:
data = ["389125467"]

data = list(data[0])
data = [int(line) for line in data]

size = 1000000
# selected cup
# remove next three in the list
# find destination cup (next lowest number)
# place the three cups in the spots after the destination cup
# next cup is directly clockwise of current cup


# make data have all the numbers
num = 10
while num < 1000000:
    data += [num]
    num += 1
data += [num]


current = data[0]
curIndex = 0
cups = CupList(copy.deepcopy(data))
#cups.printAll()

print("starting actual loop")
ii = 0
while(ii < 10000000):
    extracted = cups.getSubList( curIndex )
    curIndexCopy = copy.deepcopy(curIndex)
#    cups.printAll()
    print("Current cup:",current)
    print("Extracted:",extracted)
    dest = cups.getDestination( current, extracted )
    print("Destination:",dest)
    
    # shift the cups up to and including destination cup
    # this while loop only handles UP TO the destination cup
    while cups.get(curIndex + 4) != dest:
        cups.set(curIndex + 1, cups.get(curIndex + 4))
        curIndex += 1
        
    # aaaand move the destination cup too
    cups.set(curIndex + 1, cups.get(curIndex + 4))
    curIndex += 2
    
    # then set the extracted cups back into place
    for jj in range(len(extracted)):
        cups.set(curIndex + jj, extracted[jj])
#    cups.printAll()

    # next cups should be at current cup's index + 1
    curIndex = copy.deepcopy(curIndexCopy) + 1
    current = cups.get(curIndex)

    ii += 1
    print(ii)

cups.finish()
