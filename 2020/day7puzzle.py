

def hasShinyGold( graph, key ):
    values = graph[key]
    if values == ["other bags."]:
        return False
    elif "shiny gold" in values:
        return True
    else:
        for value in values:
            if( hasShinyGold( graph, value )):
                return True
        return False

def addBagsOfBags( graph, bag ):
#    print(bag)
    if( graph[bag][0] == 0 ):
        return 0
    totalBags = graph[bag][0]
    for ii in range(len(graph[bag][1][1])):
        totalBags = totalBags + int(graph[bag][1][0][ii]) * addBagsOfBags(graph, graph[bag][1][1][ii])
    return totalBags        
    

f = open("day7.txt")
data = f.readlines()
f.close()

# time to learn about graphs in python
# don't need a graph, I can implement with a dictionary
# basically an adjacency list where each key has a list of values

graph = {}

# need to read in each line. The first color is the key,
# all the other colors are values.

data = [line.strip() for line in data]
data = [line.split(' ') for line in data]
keys = [line[0] + " " + line[1] for line in data]
sudovalues = [line[4:] for line in data]


# part 2 needs to parse the sudovalues slightly differently
# we need to know how many of each bag is contained
# store in dictionary as the following
# bag (contains:) [ [total num bags], [[num bag], [bag color]] ]
#print( sudovalues )

values = []
bags = []
ii = 0
for line in sudovalues:
    jj = 0
    value = []
    bag = []
    while jj < len(line):
#        print(ii, jj, jj+1)
#        print(line)
        bag += [line[jj]]
        value += [line[jj+1] + " " + line[jj+2]]
        jj += 4
    values += [value]
    bags += [bag]
    ii += 1

#print(bags)
#print()
#print(values)


for ii in range(len(keys)):
    totalBags = 0
    for jj in range(len(bags[ii])):
        if bags[ii][jj] == "no":
            pass
        else:
            totalBags += int(bags[ii][jj])
    graph[ keys[ii] ] = [totalBags, [bags[ii], values[ii]] ]

#print(" Bag    total bags   num of each bag      color of bags\n")
#for key in graph:
#    print(key, ":", graph[key])
#    print(graph[key][0])

print(addBagsOfBags( graph, "shiny gold" ))

kill


# part 1 parsing
values = []
ii = 0
for line in sudovalues:
    jj = 0
    value = []
    while jj < len(line):
#        print(ii, jj, jj+1)
#        print(line)
        value += [line[jj] + " " + line[jj+1]]
        jj += 4
    values += [value]
    ii += 1
    
#print(len(keys))
#print(keys)
#print(len(values))
#print(values)

for ii in range(len(keys)):
    graph[ keys[ii] ] = values[ii]

#print()
#print()
#print(graph)
#print("Light red contains:", graph["light red"])
        
# go through every key in the dictionary and see if it eventually contains "shiny gold"
total = 0
for key in graph:
    if( hasShinyGold( graph, key )):
        total += 1

print(total, "which should be less than", len(graph))



#print("your code is working perfectly. thank Napsia and scmooch her")
      
