

import math


f = open("day13.txt")
data = f.readlines()
f.close()

departTime = int(data[0])
nums = data[1].split(',')
nums[-1] = nums[-1].strip()
print(nums)
busNums = []
for num in nums:
	if num != 'x':
		busNums += [int(num)]
		#print(num, ":", nums.index(num) )



print(busNums)


maxBus = max(busNums)
index = nums.index(str(maxBus))


testtime = busNums[0]
testtime = int(testtime)
increment = busNums[0]
increment = int(increment)
ii = 1
while(ii < len(busNums)):
        while( ((testtime + nums.index(str(busNums[ii]))) % busNums[ii]) != 0 ):
                testtime += increment
        increment = int(increment)
        increment = (increment * busNums[ii]) / math.gcd(increment, busNums[ii])
        ii += 1
print(testtime)
kill



print("maxBus:", maxBus)
print("index: ", index)

testtime = 0
foundIt = False
while not foundIt:
        testtime += maxBus
        
        findingIt = True
        for bus in busNums:
                tmp = testtime - index + nums.index(str(bus))
                if tmp % bus != 0:
                        findingIt = False
                        break
        foundIt = findingIt
        if testtime % 647000000 == 0:
                print(testtime)

testtime -= index
print(testtime)
kill


testtime = 0
foundIt = False
while not foundIt:
        testtime += busNums[0]
        
        findingIt = True
        for bus in busNums:
                tmp = testtime + nums.index(str(bus))
                if tmp % bus != 0:
                        findingIt = False

        foundIt = findingIt


print(testtime)


kill
# now we need to figure out the soonest time we can take each busNum

busTimes = []
for bus in busNums:
        busTime = 0
        while busTime < departTime:
                busTime += bus
        busTimes += [busTime]

print("Departure time:", departTime)
print(busTimes)

# then subtract the departTime from the busTimes to see how long
# we will have to wait for each individual bus to arrive

for ii in range(len(busTimes)):
        busTimes[ii] = busTimes[ii] - departTime

print(busTimes)

minIndex = busTimes.index(min(busTimes))

print(busTimes[minIndex] * busNums[minIndex])
