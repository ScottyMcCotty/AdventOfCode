




f = open("day12.txt")
data = f.readlines()

x = 0
wx = 10
y = 0
wy = 1
angle = 0


#line = data[1]
#line = line.strip()
#command = line[0]
#amount = line[1:]
#print(command)
#print(amount)

for line in data:
    line = line.strip()
    command = line[0]
    amount = int(line[1:])

    # command is N, E, S, W or R, L, or F
    # NESW is movement in that direction
    if( command == 'N' ):
        #y = y + amount
        wy = wy + amount
    elif( command == 'E' ):
        #x = x + amount
        wx = wx + amount
    elif( command == 'S' ):
        #y = y - amount
        wy = wy - amount
    elif( command == 'W' ):
        #x = x - amount
        wx = wx - amount
    # RL is rotation in the designated direction
    elif( command == 'R' ):
        dx = wx - x
        dy = wy - y
        if( amount == 90 ):
            # the x offset amount becomes the y offset amount
            # the y offset amount is negative x offset amount
            wx = x + dy
            wy = y - dx
        elif( amount == 180 ):
            # x offset amount is negative of x offset amount
            # y offset amount is negative of y offset amount
            wx = x - dx
            wy = y - dy
        elif( amount == 270 ):
            # the x offset amount is negative y offset amount
            # the y offset amount becomes the x offset amount
            wx = x - dy
            wy = y + dx
    elif( command == 'L' ):
        dx = wx - x
        dy = wy - y
        if( amount == 90 ):
            # should be same as R 270
            wx = x - dy
            wy = y + dx
        elif( amount == 180 ):
            # should be same as R 180
            wx = x - dx
            wy = y - dy
        elif( amount == 270 ):
            # should be same as R 90
            wx = x + dy
            wy = y - dx
    # F is movement in the direction of the angle
    elif( command == 'F' ):
        # direction % 360 is either 0, 90, 180, or 270
        # need to move the ship to the waypoint the number of times
        dx = wx - x
        dy = wy - y
        x = x + dx * amount
        wx = wx + dx * amount
        y = y + dy * amount
        wy = wy + dy * amount
        
    else:
        print("Unknown command found: ", command)
    # that should take care of all possible commands
    #print(line, " \tx:", x, "   \ty:", y, "   \twx:", wx, "   \twy:", wy, "   \tdx:", wx-x, "   \tdy:", wy-y)

print((abs(x) + abs(y)))
