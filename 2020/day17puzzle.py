
import copy


def getAdjacent( cube, ii, jj, kk ):
    total = 0

    # on same layer
    total += at(cube,ii+1,jj,kk)
    total += at(cube,ii-1,jj,kk)
    total += at(cube,ii,jj+1,kk)
    total += at(cube,ii,jj-1,kk)
    total += at(cube,ii+1,jj+1,kk)
    total += at(cube,ii-1,jj-1,kk)
    total += at(cube,ii+1,jj-1,kk)
    total += at(cube,ii-1,jj+1,kk)

    # on upper layer
    total += at(cube,ii+1,jj,kk+1)
    total += at(cube,ii-1,jj,kk+1)
    total += at(cube,ii,jj+1,kk+1)
    total += at(cube,ii,jj-1,kk+1)
    total += at(cube,ii+1,jj+1,kk+1)
    total += at(cube,ii-1,jj-1,kk+1)
    total += at(cube,ii+1,jj-1,kk+1)
    total += at(cube,ii-1,jj+1,kk+1)
    total += at(cube,ii,jj,kk+1)

    # on lower layer
    total += at(cube,ii+1,jj,kk-1)
    total += at(cube,ii-1,jj,kk-1)
    total += at(cube,ii,jj+1,kk-1)
    total += at(cube,ii,jj-1,kk-1)
    total += at(cube,ii+1,jj+1,kk-1)
    total += at(cube,ii-1,jj-1,kk-1)
    total += at(cube,ii+1,jj-1,kk-1)
    total += at(cube,ii-1,jj+1,kk-1)
    total += at(cube,ii,jj,kk-1)

    return total


def at(cube, ii, jj, kk):
    if ii < 0 or ii >= len(cube):
        return 0
    if jj < 0 or jj >= len(cube[0]):
        return 0
    if kk < 0 or kk >= len(cube[0][0]):
        return 0
    if cube[ii][jj][kk] == '#':
        return 1
    if cube[ii][jj][kk] == '.':
        return 0
    else:
        print("Unknown character detected. Run for your lives")
    return 0


def printWholeCube( cube ):
    for ii in range(len(cube)):
        for jj in range(len(cube[0])):
            print(cube[ii][jj])
        print()

def getTotalActive( cube ):
    total = 0
    for ii in range(len(cube)):
        for jj in range(len(cube[0])):
            for kk in range(len(cube[0][0])):
                if( cube[ii][jj][kk] == '#' ):
                    total += 1
    return total


f = open("day17.txt")
data = f.readlines()
datalength = len(data)
data = [['.']*7+list(line.strip())+['.']*7 for line in data]

#for line in data:
#    print(line)
#kill

blank = []
blanks = []

blankdata = []
blankdatas = []
for ii in range(len(data[0])):
    blankdata += [copy.deepcopy('.')]
    
for ii in range(7):
    blankdatas += [copy.deepcopy(blankdata)]

data = [copy.deepcopy(blankdata) for ii in range(7)] + [line for line in data] + [copy.deepcopy(blankdata) for ii in range(7)]

#for line in data:
#    print(line)
#kill
    

# create 1D rows of blanks
for ii in range(datalength+14):
    blank += [copy.deepcopy('.')]

# create 2D rows of blanks
for ii in range(datalength+14):
    blanks += [copy.deepcopy(blank)]


cube = []
for ii in range(15):
    if ii == 7:
        cube += [copy.deepcopy(data)]
    else:
        cube += [copy.deepcopy(blanks)]


#printWholeCube( cube )
#kill


# make copy of cube
# if active and 2 or 3 are active, stay active, otherwise become inactive
# if inactive and exactly 3 are active, get active, otherwise stay inactive



for turn in range(6):
    cubeCopy = copy.deepcopy(cube)
    for ii in range(len(cubeCopy)):
        for jj in range(len(cubeCopy[0])):
            for kk in range(len(cubeCopy[0][0])):
                neighbors = getAdjacent( cube, ii, jj, kk )
                if cube[ii][jj][kk] == '#':
                    # spot is currently active
                    if neighbors == 2 or neighbors == 3:
                        # nothing happens, stay active
                        pass
                    else:
                        # not correct number of neighbors, deactivate
                        cubeCopy[ii][jj][kk] = '.'
                else:
                    # spot is currently inactive
                    if neighbors == 3:
                        # activate spot
                        cubeCopy[ii][jj][kk] = '#'
                    else:
                        # nothing happens, stay inactive
                        pass

    #print the whole cube for us to see
    #print("Turn:",turn)
    #printWholeCube(cubeCopy)

    # update the status of the cube
    cube = copy.deepcopy(cubeCopy)





print(getTotalActive(cube))






