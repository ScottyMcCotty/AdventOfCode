

f = open("day3puzzle.txt")
data = f.readlines()
print("Lines: ", len(data))
print("Line size: ", len(data[0]))
f.close()


collisions = 0
xpos = 0
xchange = 1
print(data[0][0])
print(data[1][3])
print(data[2][6])
print(data[3][9])
ii = 0
iichange = 2
while(ii < len(data)):
    
    if(data[ii][ xpos % 31 ] == '#'):
        collisions += 1
    xpos += xchange
    ii += iichange

print("Collisions: ", collisions)


# 1: 84
# 2: 289
# 3: 89
# 4: 71
# 5: 36
