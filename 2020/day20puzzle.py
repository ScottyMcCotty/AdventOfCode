


import copy
import math

tileLength = 0

def buildFirstRow( tiles, tileIDs ):
    global tileLength
    # find top left corner
    # there will be 12 in the first row. Making space for each one.
    row = [0 for ii in range(tileLength)]
    rowIDs = [0 for ii in range(tileLength)]
    for tile in tiles:
        if tile.matches[0] == None and tile.matches[3] == None:
            # this must be our one and only top left tile
            print("top left corner:",tile.ID)
            print(tileIDs[tile.ID].matches)
            row[0] = copy.deepcopy(tile.lines)
            rowIDs[0] = tile.ID
            break
    # now we need to find the next element, whose ID will be at index 1 of the matches
    ii = 1
    # do all in the row except the last one
    print("Tile length:",tileLength)
    while( ii < tileLength ):
        currentTile = tileIDs[rowIDs[ii-1]]
        nextTile = tileIDs[currentTile.matches[1]]
        done = False
        while( not done ):
            if currentTile.east == nextTile.west:
                break
            if currentTile.east == nextTile.west[::-1]:
                nextTile.flip()
                break
            print("Need to rotate")
            nextTile.rotate()

        row[ii] = copy.deepcopy(nextTile.lines)
        rowIDs[ii] = nextTile.ID
        
        ii += 1
    #for r in row:
    #    for line in r:
    #        print(line)
    #    print()
    #for ids in rowIDs:
    #    print(ids)
        
    return [row, rowIDs]

def buildNextRow( tiles, tileIDs, upperLeft ):
    global tileLength
    # find top left corner
    # there will be 12 in the first row. Making space for each one.
    row = [0 for ii in range(tileLength)]
    rowIDs = [0 for ii in range(tileLength)]
    
    nextTile = tileIDs[upperLeft.matches[2]]
    done = False
    while( not done ):
        if upperLeft.south == nextTile.west[::-1]:
            nextTile.rotate()
            break
        if upperLeft.south == nextTile.west:
            nextTile.flip()
            nextTile.rotate()
            break
        #print("Need to rotate")
        nextTile.rotate()

    row[0] = copy.deepcopy(nextTile.lines)
    rowIDs[0] = nextTile.ID
    #print("Next tile's north edge:",nextTile.north)
    #print("Top tiles's south edge:",upperLeft.south)
    print(rowIDs[0])
    # now we need to find the next element, whose ID will be at index 1 of the matches
    ii = 1
    # do all in the row except the last one
    print("Tile length:",tileLength)
    while( ii < tileLength ):
        currentTile = tileIDs[rowIDs[ii-1]]
        nextTile = tileIDs[currentTile.matches[1]]
        done = False
        while( not done ):
            if currentTile.east == nextTile.west:
                break
            if currentTile.east == nextTile.west[::-1]:
                nextTile.flip()
                break
            #print("Need to rotate")
            nextTile.rotate()

        row[ii] = copy.deepcopy(nextTile.lines)
        rowIDs[ii] = nextTile.ID
        
        ii += 1
    #for r in row:
    #    for line in r:
    #        print(line)
    #    print()
    #for ids in rowIDs:
    #    print(ids)
        
    return [row, rowIDs]


def numNeighbors(tiles, tile):
    total = 0
    edges = [tile.north, tile.east, tile.south, tile.west]
    #print(edges)
    for other in tiles:
        if tile.ID == "Tile 2729:" and other.ID == "Tile 1951:":
            #print("You better match")
            #print(other.north)
            #print()
            #print(tile.south)
            if( other.north == tile.south ):
                print("I really should be updating",other.ID)
                print(other.matches)
        if other.ID == "Tile 2729:" and tile.ID == "Tile 1951:":
            #print("You better match")
            #rint(other.south)
            #print()
            #print(tile.north)
            if( other.south == tile.north ):
                print("I really should update",other.ID)
                print(other.matches)
                
        if tile.ID == other.ID:
            continue
        for edge in edges:
            
            if edge == other.north or edge[::-1] == other.north:
                if( other.matches[0] != None ):
                    print("overwriting a north edge :(")
                total += 1
                other.matches[0] = tile.ID
                #print(tile.ID,"matches",other.ID,"'s north edge")
                
            elif edge == other.east or edge[::-1] == other.east:
                total += 1
                if( other.matches[1] != None ):
                    print("overwriting an east edge :(")
                other.matches[1] = tile.ID
                #print(tile.ID,"matches",other.ID,"'s east edge")
                
            elif edge == other.south or edge[::-1] == other.south:
                if( other.matches[2] != None ):
                    print("overwriting a south edge :(")
                total += 1
                other.matches[2] = tile.ID
                #print(tile.ID,"matches",other.ID,"'s south edge")
                
            elif edge == other.west or edge[::-1] == other.west:
                if( other.matches[3] != None ):
                    print("overwriting a west edge :(")
                total += 1
                other.matches[3] = tile.ID
                #print(tile.ID,"matches",other.ID,"'s west edge")

        if ((other.ID == "Tile 2729:" and tile.ID == "Tile 1951:") or (other.ID == "Tile 1951:" and tile.ID == "Tile 2729:")):
            print("Now I have updated",other.ID)
            print(other.matches)
    return total


def flipOcean( ocean ):
    # does a horizontal flip over the middle of the map
    newocean = copy.deepcopy(ocean)

    for ii in range(len(ocean)):
        newocean[len(ocean)-1-ii] = copy.deepcopy( ocean[ii] )
    return newocean


def rotateOcean( ocean ):
    # does a single clockwise rotation
    newocean = copy.deepcopy(ocean)
    for ii in range(len(ocean)):
        for jj in range(len(ocean[0])):
            newocean[jj][abs(len(ocean)-ii-1)] = ocean[ii][jj]
    return newocean


def get( ocean, ii, jj ):
    #print("Searching ocean at",ii,jj)
    if ii < 0 or ii >= len(ocean):
        return False
    if jj < 0 or jj >= len(ocean[0]):
        return False
    if ocean[ii][jj] != '#':
        return False
    return True

def findMonsters( ocean ):
## X                 # 
## #    ##    ##    ###
##  #  #  #  #  #  #   

    total = 0
    for ii in range(len(ocean)):
        for jj in range(len(ocean[0])):
            if get(ocean,ii,jj+18):
                if get(ocean,ii+1,jj) and get(ocean,ii+1,jj+5) and get(ocean,ii+1,jj+6) and get(ocean,ii+1,jj+11)\
                   and get(ocean,ii+1,jj+12) and get(ocean,ii+1,jj+17) and get(ocean,ii+1,jj+18) and get(ocean,ii+1,jj+19):
                    if get(ocean,ii+2,jj+1) and get(ocean,ii+2,jj+4) and get(ocean,ii+2,jj+7) and\
                    get(ocean,ii+2,jj+10) and get(ocean,ii+2,jj+13) and get(ocean,ii+2,jj+16):
                        total += 1
    return total

def getCount( ocean ):
    count = 0
    for ii in range(len(ocean)):
        for jj in range(len(ocean[0])):
            if ocean[ii][jj] == '#':
                count += 1
    return count
    
##        lines = copy.deepcopy(self.lines)
##        #for line in lines:
##        #    print(line)
##        #print("Doing rotation")
##        newlines = copy.deepcopy(lines)
##        for ii in range(len(lines)):
##            for jj in range(len(lines[0])):
##                newlines[jj][abs(len(lines)-ii-1)] = lines[ii][jj]
##        #for line in newlines:
##        #    print(line)
##        self.lines = copy.deepcopy(newlines)
##        self.assignEdges()
##        tmp = self.matches[0]
##        self.matches[0] = self.matches[3]
##        self.matches[3] = self.matches[2]
##        self.matches[2] = self.matches[1]
##        self.matches[1] = tmp
##        return


class Tile:
    def __init__(self, lines):
        #print(len(lines))
        #print("In constructor")
        lines = [line.strip() for line in lines]
        self.ID = lines[0]
        self.north = []
        self.east = []
        self.south = []
        self.west = []
        lines = lines[1:]
        
        self.lines = [list(line) for line in lines]
        self.matches = [None, None, None, None]
        
        self.assignEdges()
        #for ii in range(len(lines)):
        #    self.north += lines[0][ii]
        #    self.east += lines[ii][-1]
        #    self.south += lines[-1][ii]
        #    self.west += lines[ii][0]
        #print(self.ID)
        #print(self.north)
        #print(self.east)
        #print(self.south)
        #print(self.west)
        
    def assignEdges(self):
        self.north = []
        self.east = []
        self.south = []
        self.west = []
        for ii in range(len(self.lines)):
            self.north += self.lines[0][ii]
            self.east += self.lines[ii][-1]
            self.south += self.lines[-1][ii]
            self.west += self.lines[ii][0]
        return
        
    def rotate(self):
        # does a single clockwise rotation
        lines = copy.deepcopy(self.lines)
        #for line in lines:
        #    print(line)
        #print("Doing rotation")
        newlines = copy.deepcopy(lines)
        for ii in range(len(lines)):
            for jj in range(len(lines[0])):
                newlines[jj][abs(len(lines)-ii-1)] = lines[ii][jj]
        #for line in newlines:
        #    print(line)
        self.lines = copy.deepcopy(newlines)
        self.assignEdges()
        tmp = self.matches[0]
        self.matches[0] = self.matches[3]
        self.matches[3] = self.matches[2]
        self.matches[2] = self.matches[1]
        self.matches[1] = tmp
        return

    def flip(self):
        # flips over a horizontal line.
        newlines = copy.deepcopy(self.lines)
        #for line in self.lines:
        #    print(line)
        #print("Doing horizontal flip")
        for ii in range(len(self.lines)):
            newlines[len(self.lines)-1-ii] = copy.deepcopy(self.lines[ii])
        #for line in newlines:
        #    print(line)
        self.lines = copy.deepcopy(newlines)
        self.assignEdges()
        tmp = self.matches[0]
        self.matches[0] = self.matches[2]
        self.matches[2] = tmp
        return
        
f = open("day20.txt")
data = f.readlines()
data = [line.strip() for line in data]

tiles = []
currentData = []
for line in data:
    if line == '':
        #print("Adding object to tiles, reseting currentdata")
        tiles += [Tile(copy.deepcopy(currentData))]
        currentData = []
    else:
        #print("Adding line to currentdata:", line)
        currentData += [copy.deepcopy(line)]
        
tiles += [Tile(copy.deepcopy(currentData))]


print("tiles length:", len(tiles))
tileLength = int(math.sqrt(len(tiles)))

print("done")

#print(numNeighbors(tiles, tiles[0]))
#kill

counts = [0,0,0]
tileIDs = {}
for tile in tiles:
    neighbors = numNeighbors(tiles, tile)
    if neighbors == 2:
        #print(tile.ID, tile.matches)
        counts[0] += 1
        
    elif neighbors < 2:
        print("This tile had less than 2 matches. not good")
    elif neighbors == 3:
        counts[1] += 1
        #print(tile.ID, neighbors )
    elif neighbors == 4:
        counts[2] += 1
    tileIDs[tile.ID] = tile

print("Counts:",counts)

#for line in tiles[0].lines:
#    print(line)

#tiles[0].flip()
#tiles[0].flip()
#tiles[0].rotate()
#tiles[0].rotate()
#tiles[0].rotate()
#tiles[0].rotate()
#print(tiles[0].matches)
#tiles[0].rotate()
#print(tiles[0].matches)
#print()
#tiles[0].flip()
#print()
#for line in tiles[0].lines:
#    print(line)
#kill
print()
print()
#print(tileIDs["Tile 1951:"].matches)
#print(tileIDs["Tile 2311:"].matches)
#print(tileIDs["Tile 2311:"].west)

##print(tileIDs["Tile 2729:"].matches)
##print(tileIDs["Tile 2729:"].south)
##print(tileIDs["Tile 1951:"].north)

print("DONE")

rows = []
row = []
rowIDss = []
rowIDs = []

[row, rowIDs] = buildFirstRow( tiles, tileIDs )

rows += [row]
rowIDss += [rowIDs]

#print("FUCK")
for ss in rowIDss:
    for s in ss:
        pass
 #       print(s)

ii = 1
while( ii < tileLength ):
    [row, rowIDs] = buildNextRow( tiles, tileIDs, tileIDs[rowIDss[ii-1][0]] )
    rows += [row]
    rowIDss += [rowIDs]
    ii += 1
#    print("FUCK")
    for ss in rowIDss:
        for s in ss:
            pass
#            print(s)


#print("rows[0][0]:")
#for row in rows[0][0]:
#    print(row)
#print("rows[0][1]:")
#for row in rows[0][1]:
#    print(row)
#print("rows[0][2]:")
#for row in rows[0][2]:
#    print(row)
#print()


ocean = []
for ii in range(tileLength):
    for kk in range(1,9):
        maprow = []
        for jj in range(tileLength):
            #print(ii,jj,kk,"[1:-1]")
            maprow += rows[ii][jj][kk][1:-1]
        ocean += [maprow]
        #print(maprow)
        #print()


#ocean = flipOcean(ocean)

while(True):
    numMonsters = findMonsters(ocean)
    if numMonsters != 0:
        break
    ocean = rotateOcean(ocean)
    numMonsters = findMonsters(ocean)
    if numMonsters != 0:
        break
    ocean = rotateOcean(ocean)
    numMonsters = findMonsters(ocean)
    if numMonsters != 0:
        break
    ocean = rotateOcean(ocean)
    numMonsters = findMonsters(ocean)
    if numMonsters != 0:
        break
    ocean = rotateOcean(ocean)
    print("Flipping to find monsters...")
    ocean = flipOcean(ocean)

print()
print()
print(numMonsters)

monsterSize = 15
num = getCount(ocean)
print(num)
final = num - monsterSize*numMonsters
print(final)

#for row in ocean:
#    print(row)

#print(get(ocean, 0,0))
#print(get(ocean, 0,2))
#print(get(ocean, 1,1))
#print(get(ocean, len(ocean)-1,len(ocean[0])-1))


#001 + 011 + 021
#002 + 012 + 022
#003 + 013 + 023




#for row in ocean:
#    print(row)
#
#ocean = flipOcean(ocean)
#print()
#print()
#for row in ocean:
#    print(row)
#
#ocean = rotateOcean(ocean)
#print()
#print()
#for row in ocean:
#    print(row)

##
##for ss in rowIDss:
##    for s in ss:
##        print(s)

#for tile in tiles:
#    if None in tile.matches:
#        print(tile.ID,tile.matches)

#print(tiles[0].west)
#print(tiles[0].east[::-1])
#print(tiles[-1].ID, tiles[-1].west)
##for line in data:
##    print(line)
##kill
##data = ''.join(data)
##data = data.split("\n\n")
##
##for line in data:
##    print(line)
##
##ii = 0
##while(ii < len(data)):
##    subdata = data[ii:11]
##    print(subdata)
##    kill
