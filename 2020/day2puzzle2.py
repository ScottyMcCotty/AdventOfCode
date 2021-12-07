

f = open("day2puzzle1.txt")
data = f.readlines()
lines = [line.strip() for line in data]
f.close()

# now lines should be a list of lines? Let's see
#for line in lines:
    #print(line)

numSuccess = 0

for line in lines:
    [ranges, letter, word] = line.split(" ")
    [lower, upper] = ranges.split("-")
    lower = int(lower)
    upper = int(upper)
    letter = letter[0]
    #print(lower, upper, letter, word)
    #print(ranges, letter, word)
    #print(lines[999])


    if( (word[lower-1] == letter) ^ (word[upper-1] == letter) ):
        numSuccess += 1
##    occurences = 0
##    for char in word:
##        if letter == char:
##            occurences = occurences + 1
##            
##    #print(occurences)
##    if( (occurences <= upper) and (occurences >= lower) ):
##        #print("Success!")
##        numSuccess += 1

print(numSuccess)
    
