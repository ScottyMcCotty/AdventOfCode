
import copy

# Function for taking a line and parsing the Mask
# Returns the mask as a string
def getMaskFromLine( line ):
    mask = line.strip()
    mask = mask[7:]
    return mask

# Function for taking a line and parsing the contents into memory index and value
# Returns a list of two ints [index, value]
def getMemoryCommandFromLine( line ):
    [index, value] = line.split(" = ")
    
    index = index[0:-1]
    index = int(index[4:])

    value = int(value)
    
    return [index, value]


# Function for taking an int and updating it using a given mask.
# Returns the updated int.
def updateIntWithMask( num, mask ):
    # plan:
    # make the decimal value into a binary string
    # split the (immutable) string into a (mutable) list
    # make the list be 36 bits large by prepending 0's
    # replace certain elements of that list with elements from the mask
    # combine back into a string
    # convert back to int
    # store back into values[ii]

    bstring = bin(num)[2:]
    bstringlist = list(bstring)
    while( len(bstringlist) < 36 ):
        bstringlist = ['0'] + bstringlist

    for ii in range(len(mask)):
        if( mask[ii] != 'X' ):
            bstringlist[ii] = mask[ii]

    bstring = ''.join(bstringlist)
    bint = int(bstring, 2)
    return bint

def getTotalOfDictionary( dictionary ):
    total = 0
    for key in dictionary:
        total += dictionary[key]
    return total

def getAddressesFromMask( index, mask ):
    # plan:
    # make the decimal value into a binary string
    # split the (immutable) string into a (mutable) list
    # make the list be 36 bits long by prepending 0's
    # replace certain elements of that list with elements from the mask (1's and X's get copied over)
    bstring = bin(index)[2:]
    bstringlist = list(bstring)
    while( len(bstringlist) < 36 ):
        bstringlist = ['0'] + bstringlist

    for ii in range(len(mask)):
        if( mask[ii] != '0' ):
            bstringlist[ii] = mask[ii]

    # now we have a memory address but it'll have a bunch of X's in it. Every X makes two new addresses
    # this is where things get ugly...
    addresslist = [bstringlist]
    while( 'X' in addresslist[0] ):
        for ii in range(len(addresslist)):
            index = addresslist[ii].index('X')
            # make two copies
            address0 = copy.deepcopy(addresslist[ii])
            address1 = copy.deepcopy(addresslist[ii])
            address0[index] = '0'
            address1[index] = '1'
            # replace the original copy with address0
            addresslist[ii] = address0
            # append address1 onto the end
            addresslist = addresslist + [address1]
    # now we should have a list of lists of bits. The inner lists need to be recombined into ints
#    print("Addresslist:", addresslist)
    for ii in range(len(addresslist)):
        bstring = ''.join(addresslist[ii])
        bint = int(bstring, 2)
        addresslist[ii] = bint
#    print(addresslist)
    return addresslist


# read in information
f = open("day14.txt")
data = f.readlines()
f.close()


# part 2: 10885823581193 is too high apparently
# okay is 3816594901962 smaller? yes. Is it right? YEP

memory = {}
for line in data:
    if( "mask" in line ):
        # it's a mask line,
        # get the new mask
        mask = getMaskFromLine( line )
#        print("Finished a mask update line")
    else:
        # it's a memory line,
        # get the index and value
        [index, value] = getMemoryCommandFromLine( line )

        # the part 2 specialty is now we need to make a list of all possible memory addresses
        # that are being changed. The mask gets applied to the INDEX this time, and generates
        # 2^n possibilites, where n is the number of X's in the mask. Yikes
        allPossibleAddresses = getAddressesFromMask( index, mask )
#        print("allPossibleAddresses:", allPossibleAddresses)
        for address in allPossibleAddresses:
            # updating ALL the addresses
            memory[address] = value
#        print("Finished a memory access line")

print(getTotalOfDictionary( memory ))
##
##
##
### this is part 1:
##memory = {}
##for line in data:
##    if( "mask" in line ):
##        # it's a mask line,
##        # get the new mask
##        mask = getMaskFromLine( line )
##    else:
##        # it's a memory line,
##        # get the index and value
##        [index, value] = getMemoryCommandFromLine( line )
##        # update the value
##        value = updateIntWithMask( value, mask )
##        # store them in the dictionary
##        memory[index] = value
##
##
### get the total of all values in the dictionary
##total = getTotalOfDictionary( memory )
##print(memory)
##print(total)


##
##mask = data[0].strip()
##data = data[1:]
###print(mask)
##mask = mask[7:]
##print(mask)
### mask has been acquired and trimmed.
##
##memory = {}
###memory[1] = "Hello"
###print(memory)
### okay, so that's how dictionaries work. Cool
##
### strip the trailing newline character
##data = [line.strip() for line in data]
##
### remove the ' = ' from each line
##nums = [line.split(" = ") for line in data]
##
### now nums is a list of lists where
### nums[x][0] is a command (need to trip this down to just the value
### nums[x][1] is a value
##
### get all the memory accesses from the list of lists
##memaccesses = [nums[ii][0] for ii in range(len(nums))]
##
### strip the trailing ']'
##memaccesses = [access[0:-1] for access in memaccesses]
##
### strip the leading 'mem['
##memaccesses = [int(access[4:]) for access in memaccesses]
##
### now memaccesses is just a list of ints representing memory locations
##
### the new values need to be extracted from the list of lists
##values = [int(nums[ii][1]) for ii in range(len(nums))]
##
### the values need to be adjusted for the mask. This is gonna be complicated
### dammit, python strings are immutable. Maybe that'll be okay though
##
##for ii in range(len(values)):
##    # plan:
##    # make the decimal value into a binary string
##    # split the (immutable) string into a (mutable) list
##    # make the list be 36 bits large by prepending 0's
##    # replace certain elements of that list with elements from the mask
##    # combine back into a string
##    # convert back to int
##    # store back into values[ii]
##
##    bstring = bin(values[ii])[2:]
##    bstringlist = list(bstring)
##    while( len(bstringlist) < 36 ):
##        bstringlist = ['0'] + bstringlist
##
##    for jj in range(len(mask)):
##        if( mask[jj] != 'X' ):
##            bstringlist[jj] = mask[jj]
##
##    bstring = ''.join(bstringlist)
##    bint = int(bstring, 2)
##    print(ii)
##    values[ii] = bint
##
##
### make a dictionary of commands : values
##for ii in range(len(values)):
##    memory[memaccesses[ii]] = values[ii]
##
### then add all the values in the dictionary
##total = 0
##for key in memory:
##    total += memory[key]
##    
##print(total)
###print(memaccesses)
###print(values)
###print(memory)
##








