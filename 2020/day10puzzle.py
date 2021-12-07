

def getValueOfChunk( chunk ):
        # tack on a couple ones because 2 is the first
        # value in the chunk and it needs to compound off the 1's
        chunk += [1]
        chunk += [1]

        # make list of values corresponding to each index in chunk
        values = [1] * len(chunk)

        # go through chunk backwards
        ii = len(chunk)-2
        while( ii >= 0 ):
                # the value is equal to x previous values,
                # where x is the number at index ii in chunk
                value = 0
                #print("ii =", ii, "chunk[ii] =", chunk[ii])
                for x in range(1,chunk[ii]+1):
                        value += values[ii+x]
                values[ii] = value
                ii -= 1
        return values[0]


f = open("day10.txt")
data = f.readlines()
f.close()

nums = [int(line.strip()) for line in data]
nums += [0]
#print("nums:\n",nums,sep='')
nums.sort()
nums += [nums[-1] + 3]
#print("nums sorted:\n",nums,sep='')

# add on this higher number just to avoid going out of bounds
nums += [nums[-1]+10]
#print(nums)
# find the number of paths from each number to the next

# a list of branches, where the value at a specific element is
# the number of ways we can branch off from that element
branches = [0] * len(nums)

ii = 0
while( ii < len(nums)-1 ):
        numBranches = 0
        branchIndex = ii+1
        while( nums[branchIndex] <= (nums[ii] + 3) ):
                numBranches += 1
                branchIndex += 1
        branches[ii] = numBranches
        ii += 1
print(branches[0:-2])
print(getValueOfChunk(branches[0:-2]))
kill
listOfChunks = []
chunk = []
ii = len(branches)-1
while ii >= 0:
        if( (branches[ii] != 0) and (branches[ii] != 1) ):
                chunk = [branches[ii]] + chunk
        else:
                if( chunk != [] ):
                        listOfChunks = [chunk] + listOfChunks
                chunk = []
        ii -= 1
#print(listOfChunks)


#print(getValueOfChunk([3,2]))
#print(getValueOfChunk([2]))
#print(getValueOfChunk([3,2,2,2,3,2]))

total = 1
for chunk in listOfChunks:
        total = total * getValueOfChunk( chunk )
print(total)

# part 1, I think
#print("Add all branches:",sum(branches))
# goal for example is 8
# goal for example2 is 19208
##
##total = 1
##for num in branches:
##        if num != 0:
##                total = total * num
##print("Multiply all branches:",total)
##
##
##
##differences = [0] * len(nums)
##
##ii = 1
##
##while( ii < len(nums)):
##	differences[(int(nums[ii]) - int(nums[ii-1]))] += 1
##	ii += 1
##
##
##print("Totals:", differences)
##print(differences[1] * differences[3])
