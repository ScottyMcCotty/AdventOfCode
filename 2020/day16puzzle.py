
def isAllowed( value, rules ):
    for key in rules.keys():
        if value >= rules[key][0][0] and value <= rules[key][0][1]:
            #print(value, "", rules[key][0][0])
            return True
        if value >= rules[key][1][0] and value <= rules[key][1][1]:
            #print(value, ">", rules[key][1][1])
            return True
    return False

def violatesRule( value, ruleBounds ):
    value = int(value)
    # just in case

    if value >= ruleBounds[0][0] and value <= ruleBounds[0][1]:
        return False
    if value >= ruleBounds[1][0] and value <= ruleBounds[1][1]:
        return False
    return True


f = open("day16.txt")
data = f.readlines()


# store all the data in one huge line
longline = ''.join(data)

# break the data on the two double newlines
[rules, ourTicket, allTickets] = longline.split("\n\n")

#now each one needs to be split on newline characters
rules = rules.split("\n")
allTickets = allTickets.strip()
allTickets = allTickets.split("\n")
allTickets = allTickets[1:]
rules = [line.split(":") for line in rules]
#print(rules)
ruleRanges = [line[1][1:] for line in rules]
ruleNames = [line[0] for line in rules]
#print(ruleRanges)
ruleRanges = [line.split(" or ") for line in ruleRanges]
lower = [line[0] for line in ruleRanges]
upper = [line[1] for line in ruleRanges]
lower = [line.split("-") for line in lower]
upper = [line.split("-") for line in upper]
lower1 = [int(line[0]) for line in lower]
upper1 = [int(line[1]) for line in lower]
lower2 = [int(line[0]) for line in upper]
upper2 = [int(line[1]) for line in upper]

# now make an empty dictionary of rules
rules = {}

for ii in range(len(ruleNames)):
    rules[ruleNames[ii]] = [[int(lower1[ii]),int(upper1[ii])],[int(lower2[ii]),int(upper2[ii])]]



allTickets = [line.split(',') for line in allTickets]

#print(rules)
#print(allTickets)

total = 0
validTickets = []
for ticket in allTickets:
    valid = True
    for number in ticket:
        if not isAllowed( int(number), rules ):
            #print(int(number),"is invalid")
            total += int(number)
            valid = False
    if valid and ticket not in validTickets:
        validTickets += [ticket]

#print(allTickets)
#print(validTickets)





matches = {}

for rule in rules.keys():
    # for every rule we have, to check whether the same index of every ticket passes it



    for ii in range(len(validTickets[0])):
        # ii takes on values 0 to number of entries in a ticket
        
        # let's guess the rule does match at each index
        matchesAll = True
        
        for ticket in validTickets:
            # ticket now takes on every value of ticket
            if violatesRule( ticket[ii], rules[rule] ):
                #print(ticket[ii], "violated", rules[rule])
                matchesAll = False
                break
        if matchesAll:
            if rule not in matches.keys():
                matches[rule] = [ii]
            else:
                matches[rule] += [ii]
        
#print("Matches:", matches)

ourTicket = ourTicket.split("\n")
ourTicket = ourTicket[1]
ourTicket = ourTicket.split(",")
print("My ticket:", ourTicket)
print("Matches:")
for match in matches:
    matches[match] = list(matches[match])
    print(match, ":", matches[match])
    


#for match in matches:
#    print(match,":",ourTicket[matches[match]])


altered = True
while(altered):
    altered = False
    for match in matches:
        if len(matches[match]) == 1:
            elementToRemove = matches[match][0]
            currentMatch = match
            matches[match] += [ourTicket[elementToRemove]]
    for match in matches:
        if match == currentMatch:
            continue
        else:
            tmp = matches[match]
            if elementToRemove in tmp:
                tmp.remove(elementToRemove)
                #matches[match] = matches[match].remove(elementToRemove)
                matches[match] = tmp
                #print("Removing",elementToRemove,"from",match)
                altered = True
    #for match in matches:
        #print(match, ":", matches[match])
    print("Looping")
    #dumbdumb = input("Waiting to continue")

total = 1
for match in matches:
    if "departure" in match:
        total *= int(matches[match][1])
    

print(total)

# need a list of

# for each value in a ticket, if the value is invalid for a set of rules, that 


#print(total)




#printing the answer will look like:
#for key in rules.keys():
#    if "departure" in key:
#        print(


#print(rulesNames)
#print(lower1, upper1)
#print(lower2, upper2)

#ourTicket = ourTicket.split("\n")
#ourTicket = ourTicket[1]

#allTickets = allTickets.split("\n")
#allTickets = allTickets[1:]

#print("\nRules", rules)
#print("\nMy ticket", ourTicket)
#print("\nAll tickets", allTickets)




##departure location : [19] == 19 -> 79
##departure station : [ 10, ] == 10 -> 211
##departure platform : [ 5,] -> 167
##departure track : [  11, ] -> 127
##departure date : [ 6, ] -> 181
##departure time : [ 16 ] == 16 -> 83
##arrival location : [0,]
##arrival station : [ 1, 3, 5, 6, , 9, 10, 11, 12, 13, 14, 16, 17, 19]
##arrival platform : [7]
##arrival track : [1, 3, 5, 6, , 10, 11, 16, 17, 19]
##class : [1, 3, 5, 6, 9, 10, 11, 12, 13, 16, 17, 19]
##duration : [8]
##price : [ 4,]
##route : [ 5, 6, 8, 10, 11, 16, 17, 19]
##row : [2, ]
##seat : [ 3, 5, 6, , 10, 11, 16, 17, 19]
##train : [1, 3, 5, 6, 9, 10, 11, 12, 16, 17, 19]
##type : [1, 3, 5, 6, 9, 10, 11, 16, 17, 19]
##wagon : [15]
##zone : [18]


# 848 is too low
