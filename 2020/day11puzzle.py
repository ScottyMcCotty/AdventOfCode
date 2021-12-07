
import copy


def FillSeatRecursive( data ):
    newdata = copy.deepcopy( data )
    #print(newdata)
    for ii in range(len(data)):
        for jj in range(len(data[0])):
            adj = getNumAdjacent( data, ii, jj )
            if data[ii][jj] == 'L' and adj == 0:
                newdata[ii][jj] = '#'
                #print("Adding person")
            elif data[ii][jj] == '#' and adj >= 5:
                newdata[ii][jj] = 'L'
    #print(newdata)
    #print()
    #print(data)
    #kill
    sameList = True
    for ii in range(len(data)):
        for jj in range(len(data[0])):
            if data[ii][jj] != newdata[ii][jj]:
                sameList = False
    if sameList:
        print("They're the same list, apparently")
        return CountAllOccupied( newdata )
    else:
        #print("Calling recursive function again")
        return FillSeatRecursive( newdata )

            
def getNumAdjacent( data, ii, jj ):
    adj = 0
    adj += get( data, ii, -1, jj, -1 )
    adj += get( data, ii, -1, jj, 0  )
    adj += get( data, ii, -1, jj, 1  )
    adj += get( data, ii,  0, jj, 1  )
    adj += get( data, ii,  1, jj, 1  )
    adj += get( data, ii,  1, jj, 0  )
    adj += get( data, ii,  1, jj, -1 )
    adj += get( data, ii,  0, jj, -1 )
    return adj


def CountAllOccupied( data ):
    occupied = 0
    for line in data:
        for char in line:
            if char == '#':
                occupied += 1
    return occupied


def get( data, ii, dii, jj, djj ):
    ii += dii
    jj += djj
    if ii < 0 or jj < 0 or ii >= len(data) or jj >= len(data[0]):
        return 0
    if data[ii][jj] == '#':
        # it's the first seat they can see, and it's full,
        # so it will contribute to the adjacency count
        return 1
    if data[ii][jj] == 'L':
        # it's the first seat they can see, and it's empty,
        # so it will not contribute to the adjacency count
        return 0
    return get( data, ii, dii, jj, djj)

f = open("day11.txt")
data = f.readlines()
data2 = [line.strip() for line in data]
data3 = [list(line) for line in data2]
#print(data3)
print()
f.close()


testdata = [['#', '.', '#', '.', '.', '#', '#', '.', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '.', '#', '.', '.', '#', '.', '.'],
            ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '#', '#'],
            ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '#', '#', '#', '#', '#', '#', '.', '.'],
            ['#', '.', '#', '#', '#', '#', '#', '.', '.', '#']]

#print(getNumAdjacent(testdata, 0, 0))
#print(getNumAdjacent(testdata, 0, 2))
#print(getNumAdjacent(testdata, 7, 8))
#FillSeatRecursive( testdata )
           
print( FillSeatRecursive( data3 ) )

# 137 is too low 

# day 14:
# bus 23 is 7 minute wait
# bus 41 is 29 minute wait
# bus 647 is 6 minute wait
# bus 13 is 7 minute wait
# bus 19 is 8 minute wait
# bus 29 is 9 minute wait
# bus 557 is 330 minute wait
# bus 37 is 7 minute wait
# bus 17 is 14 minute wait



#  L.LL.
#  L..LL
#  L.L.L
#  LLLL.

#  #.##.
#  #..##
#  #.#.#
#  ####.
