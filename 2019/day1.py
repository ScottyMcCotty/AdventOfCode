

def getfuel( mass ):
    fuel = (mass//3) - 2
    if( fuel <= 0 ):
        return 0
    return fuel + getfuel( fuel )

f = open("day1.txt")
data = f.readlines()


print("Mass of 12 needs:", getfuel(12))
print("Mass of 14 needs:", getfuel(20))
print("Mass of 1969 needs:", getfuel(1969))
ii = 0
total = 0
while( ii < len(data) ):
    
    total += getfuel( int(data[ii]) )
    ii += 1

print(total)
