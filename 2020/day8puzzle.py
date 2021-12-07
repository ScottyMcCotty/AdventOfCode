
import copy


def getAccumulatorInfiniteLoop( data ):
        visited = [False] * len( data )
        accumulator = 0
        ii = 0
        while True:
                if visited[ii]:
                        break
                else:
                        if( data[ii][:3] == "nop" ):
                                ii += 1
                        elif( data[ii][:3] == "acc" ):
                                accumulator += int(data[ii][4:])
                                visited[ii] = True
                                ii += 1
                        elif( data[ii][:3] == "jmp" ):
                                visited[ii] = True
                                ii += int(data[ii][4:])
                        else:
                                print("This is bad")
                if( ii == len(data) ):
                        return accumulator
        # the loop was infinite, so we broke out and return 0
        return 0



f = open( "day8.txt" )
data = f.readlines()
data = [line.strip() for line in data]


for ii in range(len(data)):
        if "nop" in data[ii]:
                altString = "jmp"
        elif "jmp" in data[ii]:
                altString = "nop"
        else:
                continue
        alternativeData = copy.deepcopy(data)
        alternativeData[ii] = altString + data[ii][3:]
        accum = getAccumulatorInfiniteLoop( alternativeData )
        if( accum != 0 ):
                print(accum)
                break
