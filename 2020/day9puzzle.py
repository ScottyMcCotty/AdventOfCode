

def getsSummedByPrevious( data, index, preamble ):
    ii = index - preamble
    while ii < index:
        jj = index - preamble
        while jj < index:
            if data[ii] + data[jj] == data[index]:
                #print(data[ii],"+",data[jj],"=",data[index])
                return True
            else:
                #print(data[ii],"+",data[jj],"!=",data[index])
                pass
            jj += 1
        ii += 1
    #print(data[ii],"wasn't summed by any of",data[index-preamble:index])
    return False


def hasContiguousSum( data, index, brokenNumber ):
    total = [data[index]]
    while sum(total) < brokenNumber:
        index += 1
        total += [data[index]]
    if sum(total) == brokenNumber:
        print(sum(total),total,"=",brokenNumber)
        print(min(total)+max(total))
        return True
    return False

f = open( "day9.txt" )
data = f.readlines()
data = [int(line.strip()) for line in data]
f.close()

preamble = 25
ii = preamble

while( ii < len(data) ):
    if not getsSummedByPrevious( data, ii, preamble ):
        print(data[ii])
        break
    ii += 1

print("None were found. That's odd")

brokenNumber = 1309761972
#brokenNumber = 127
ii = 0

while not hasContiguousSum(data, ii, brokenNumber):
    ii += 1

