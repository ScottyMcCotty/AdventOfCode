
import copy


def getAdjacent( cube, ii, jj, kk, ll ):
    total = 0

    # on same layer 8
    total += at(cube,ii+1,jj,kk,ll)
    total += at(cube,ii-1,jj,kk,ll)
    total += at(cube,ii,jj+1,kk,ll)
    total += at(cube,ii,jj-1,kk,ll)
    total += at(cube,ii+1,jj+1,kk,ll)
    total += at(cube,ii-1,jj-1,kk,ll)
    total += at(cube,ii+1,jj-1,kk,ll)
    total += at(cube,ii-1,jj+1,kk,ll)

    # on upper layer 9
    total += at(cube,ii+1,jj,kk+1,ll)
    total += at(cube,ii-1,jj,kk+1,ll)
    total += at(cube,ii,jj+1,kk+1,ll)
    total += at(cube,ii,jj-1,kk+1,ll)
    total += at(cube,ii+1,jj+1,kk+1,ll)
    total += at(cube,ii-1,jj-1,kk+1,ll)
    total += at(cube,ii+1,jj-1,kk+1,ll)
    total += at(cube,ii-1,jj+1,kk+1,ll)
    total += at(cube,ii,jj,kk+1,ll)

    # on lower layer 9
    total += at(cube,ii+1,jj,kk-1,ll)
    total += at(cube,ii-1,jj,kk-1,ll)
    total += at(cube,ii,jj+1,kk-1,ll)
    total += at(cube,ii,jj-1,kk-1,ll)
    total += at(cube,ii+1,jj+1,kk-1,ll)
    total += at(cube,ii-1,jj-1,kk-1,ll)
    total += at(cube,ii+1,jj-1,kk-1,ll)
    total += at(cube,ii-1,jj+1,kk-1,ll)
    total += at(cube,ii,jj,kk-1,ll)

    # LL - 1
    # on same layer 9
    total += at(cube,ii+1,jj,kk,ll-1)
    total += at(cube,ii-1,jj,kk,ll-1)
    total += at(cube,ii,jj+1,kk,ll-1)
    total += at(cube,ii,jj-1,kk,ll-1)
    total += at(cube,ii+1,jj+1,kk,ll-1)
    total += at(cube,ii-1,jj-1,kk,ll-1)
    total += at(cube,ii+1,jj-1,kk,ll-1)
    total += at(cube,ii-1,jj+1,kk,ll-1)
    total += at(cube,ii,jj,kk,ll-1)

    # on upper layer 9
    total += at(cube,ii+1,jj,kk+1,ll-1)
    total += at(cube,ii-1,jj,kk+1,ll-1)
    total += at(cube,ii,jj+1,kk+1,ll-1)
    total += at(cube,ii,jj-1,kk+1,ll-1)
    total += at(cube,ii+1,jj+1,kk+1,ll-1)
    total += at(cube,ii-1,jj-1,kk+1,ll-1)
    total += at(cube,ii+1,jj-1,kk+1,ll-1)
    total += at(cube,ii-1,jj+1,kk+1,ll-1)
    total += at(cube,ii,jj,kk+1,ll-1)

    # on lower layer 9
    total += at(cube,ii+1,jj,kk-1,ll-1)
    total += at(cube,ii-1,jj,kk-1,ll-1)
    total += at(cube,ii,jj+1,kk-1,ll-1)
    total += at(cube,ii,jj-1,kk-1,ll-1)
    total += at(cube,ii+1,jj+1,kk-1,ll-1)
    total += at(cube,ii-1,jj-1,kk-1,ll-1)
    total += at(cube,ii+1,jj-1,kk-1,ll-1)
    total += at(cube,ii-1,jj+1,kk-1,ll-1)
    total += at(cube,ii,jj,kk-1,ll-1)

    # LL + 1
    # on same layer 9
    total += at(cube,ii+1,jj,kk,ll+1)
    total += at(cube,ii-1,jj,kk,ll+1)
    total += at(cube,ii,jj+1,kk,ll+1)
    total += at(cube,ii,jj-1,kk,ll+1)
    total += at(cube,ii+1,jj+1,kk,ll+1)
    total += at(cube,ii-1,jj-1,kk,ll+1)
    total += at(cube,ii+1,jj-1,kk,ll+1)
    total += at(cube,ii-1,jj+1,kk,ll+1)
    total += at(cube,ii,jj,kk,ll+1)

    # on upper layer 9
    total += at(cube,ii+1,jj,kk+1,ll+1)
    total += at(cube,ii-1,jj,kk+1,ll+1)
    total += at(cube,ii,jj+1,kk+1,ll+1)
    total += at(cube,ii,jj-1,kk+1,ll+1)
    total += at(cube,ii+1,jj+1,kk+1,ll+1)
    total += at(cube,ii-1,jj-1,kk+1,ll+1)
    total += at(cube,ii+1,jj-1,kk+1,ll+1)
    total += at(cube,ii-1,jj+1,kk+1,ll+1)
    total += at(cube,ii,jj,kk+1,ll+1)

    # on lower layer 9
    total += at(cube,ii+1,jj,kk-1,ll+1)
    total += at(cube,ii-1,jj,kk-1,ll+1)
    total += at(cube,ii,jj+1,kk-1,ll+1)
    total += at(cube,ii,jj-1,kk-1,ll+1)
    total += at(cube,ii+1,jj+1,kk-1,ll+1)
    total += at(cube,ii-1,jj-1,kk-1,ll+1)
    total += at(cube,ii+1,jj-1,kk-1,ll+1)
    total += at(cube,ii-1,jj+1,kk-1,ll+1)
    total += at(cube,ii,jj,kk-1,ll+1)
    
    return total


def at(cube, ii, jj, kk, ll):
    if ii < 0 or ii >= len(cube):
        return 0
    if jj < 0 or jj >= len(cube[0]):
        return 0
    if kk < 0 or kk >= len(cube[0][0]):
        return 0
    if ll < 0 or ll >= len(cube[0][0][0]):
        return 0
    if cube[ii][jj][kk][ll] == '#':
        return 1
    if cube[ii][jj][kk][ll] == '.':
        return 0
    else:
        print("Unknown character detected. Run for your lives")
    return 0


def printWholeHyperCube( cube ):
    for ii in range(len(cube)):
        for jj in range(len(cube[0])):
            for kk in range(len(cube[0][0])):
                print(cube[ii][jj][kk])
            print()
        print()
        print()

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
                for ll in range(len(cube[0][0][0])):
                    if( cube[ii][jj][kk][ll] == '#' ):
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

# create 3D cube of blanks
cube = []
for ii in range(17):
    if ii == 8:
        cube += [copy.deepcopy(data)]
    else:
        cube += [copy.deepcopy(blanks)]
        
print("Cube is",len(cube),"x",len(cube[0]),"x",len(cube[0][0]),"x",len(cube[0][0][0]))

hypercube = []
blankcube = []

for ii in range(len(cube)):
    blankcube += [copy.deepcopy(blanks)]

print("Making hypercube now")
for ii in range(17):
    if ii == 8:
        hypercube += [copy.deepcopy(cube)]
    else:
        hypercube += [copy.deepcopy(blankcube)]
    #print("Finished layer",ii)

print("Hypercube is:",len(hypercube),"x",len(hypercube[0]),"x",len(hypercube[0][0]),"x",len(hypercube[0][0][0]))

#printWholeCube( cube )
#kill


# make copy of cube
# if active and 2 or 3 are active, stay active, otherwise become inactive
# if inactive and exactly 3 are active, get active, otherwise stay inactive



for turn in range(6):
    #cubeCopy = copy.deepcopy(cube)
    hypercubeCopy = copy.deepcopy(hypercube)
    for ii in range(len(hypercubeCopy)):
        for jj in range(len(hypercubeCopy[0])):
            for kk in range(len(hypercubeCopy[0][0])):
                for ll in range(len(hypercubeCopy[0][0][0])):
                    neighbors = getAdjacent( hypercube, ii, jj, kk, ll )
                    if hypercube[ii][jj][kk][ll] == '#':
                        # spot is currently active
                        if neighbors == 2 or neighbors == 3:
                            # nothing happens, stay active
                            pass
                        else:
                            # not correct number of neighbors, deactivate
                            hypercubeCopy[ii][jj][kk][ll] = '.'
                    else:
                        # spot is currently inactive
                        if neighbors == 3:
                            # activate spot
                            hypercubeCopy[ii][jj][kk][ll] = '#'
                        else:
                            # nothing happens, stay inactive
                            pass

    #print the whole cube for us to see
    print("Turn:",turn)
    #printWholeCube(cubeCopy)

    # update the status of the cube
    #printWholeCube(hypercubeCopy[7])
    #printWholeCube(hypercubeCopy[8])
    #print(getTotalActive(hypercubeCopy))
    #kill
    hypercube = copy.deepcopy(hypercubeCopy)





print(getTotalActive(hypercube))






