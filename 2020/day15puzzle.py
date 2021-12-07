

starting = [5,2,8,16,18,0,1]
turn = 2


spoken = {}
for num in starting:
        spoken[num] = turn
        turn += 1

currentNum = 0
#print(turn, ":", currentNum)
#spoken[currentNum] = turn

#print(spoken)
while( turn <= 30000000 ):
        if currentNum in spoken.keys():
                tmp = turn - spoken[currentNum]
                spoken[currentNum] = turn
                currentNum = tmp
        else:
                spoken[currentNum] = turn
#                print("Adding", currentNum, "to dictionary")
                currentNum = 0
        #if(turn > 2010):
                #print(turn, ":", currentNum)
        turn += 1


#print(spoken)
print(currentNum)
