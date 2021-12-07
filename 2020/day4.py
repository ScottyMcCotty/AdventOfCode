
# ''.join(list)

def extract( data ):
    ii = 0
    while(ii < len(data) and data[ii] != '\n'):
        ii += 1
#    print("\nBailed because data[",ii,"] = ",data[ii],sep='')
#    print("And extracted data: ", data[0:ii])
    return data[0:ii]

def extractfrom( data, start ):
    ii = start
    while(ii < len(data) and data[ii] != '\n'):
        ii += 1
    return (data[start:ii], ii+1)

def snip( data ):
    ii = 0
    while(ii < len(data) and data[ii] != '\n'):
        ii += 1
    return data[ii+1:-1]

def validdata( data ):
    if( validbyr(data) ):
        if( validiyr(data) ):
            if( valideyr(data) ):
                if( validhgt(data) ):
                    if( validhcl(data) ):
                        if( validecl(data) ):
                            if( validpid(data) ):
                                return True
    return False

def validbyr( data ):
    tmp = data.split("byr:")
    if( len(tmp) == 1 ):
#        print("No byr")
        return False
    tmp = tmp[1]
    tmp = int(tmp[0:4])
    #print(tmp)
    if( tmp < 1920 or tmp > 2002 ):
#        print("Invalid byr")
        return False
    return True

def validiyr( data ):
    tmp = data.split("iyr:")
    if( len(tmp) == 1 ):
#        print("No iyr")
        return False
    tmp = tmp[1]
    tmp = int(tmp[0:4])
    if( tmp < 2010 or tmp > 2020 ):
#        print("Invalid iyr")
        return False
    return True

def valideyr( data ):
    tmp = data.split("eyr:")
    if( len(tmp) == 1 ):
#        print("No eyr")
        return False
    tmp = tmp[1]
    tmp = int(tmp[0:4])
    if( tmp < 2020 or tmp > 2030 ):
#        print("Invalid eyr")
        return False
    return True

def validhgt( data ):
    tmp = data.split("hgt:")
    if( len(tmp) == 1 ):
#        print("No hgt")
        return False
    tmp = tmp[1]
    if( "cm" not in tmp and "in" not in tmp ):
#        print("No hgt units")
        return False
    if( len(tmp) > 5 ):
        tmp = tmp[0:5]
    if "cm" in tmp:
        tmp = tmp.split("cm")
        tmp = tmp[0]
        tmp = int(tmp)
        if( tmp < 150 or tmp > 193 ):
#            print("Invalid hgt")
            return False
    else:
        tmp = (tmp.split("in"))[0]
        tmp = int(tmp)
        if( tmp < 59 or tmp > 76 ):
#            print("Invalid hgt")
            return False
    return True

def validhcl( data ):
    tmp = data.split("hcl:")
    if( len(tmp) == 1 ):
#        print("No hcl")
        return False
    tmp = tmp[1]
    tmp = (tmp.split(' '))[0]
    if( len(tmp) != 7 and tmp[0] != '#' ):
#        print("Invalid hcl:", tmp)
        return False
    if( (tmp[1:7]).isalnum() ):
        for char in "ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if char in tmp[1:7]:
#                print("MY MISSING FUCKING VALUES")
                return False
        return True
#    print("hcl is NOT VALID")
    return False

def validecl( data ):
    tmp = data.split("ecl:")
    if( len(tmp) == 1 ):
#        print("No ecl")
        return False
    tmp = tmp[1]
    tmp = (tmp.split(' '))[0]
    if tmp[0:3] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
#        print("Valid ecl:--", tmp[0:3], "--",sep='')
        return True
#    print("Invalid ecl:", tmp[0:3])
    return False

def validpid( data ):
    tmp = data.split("pid:")
    if( len(tmp) == 1 ):
#        print("No pid")
        return False
    tmp = tmp[1]
    tmp = tmp.split(' ')
    tmp = tmp[0]
#    print(tmp)
    if(len(tmp) != 9):
#        print("pid length != 9")
        return False
    if(tmp[0:9]).isnumeric():
        return True
#    print("Invalid pid:", tmp[0:9])
    return False


entries = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
valid = 0
print('\t',validbyr("\nbyr:2002   "))
print('\t',validbyr("\nbyr:2003   "))
print('\t',validhgt("\nhgt:60in   "))
print('\t',validhgt("\nhgt:190cm   "))
print('\t',validhgt("\nhgt:190in   "))
print('\t',validhgt("\nhgt:190   "))
print('\t',validhcl("\nhcl:#123abc   "))
print('\t',validhcl("\nhcl:#123abz   "))
print('\t',validhcl("\nhcl:123abc   "))
print('\t',validecl("\necl:brn   "))
print('\t',validecl("\necl:wat   "))
print('\t',validpid("\npid:000000001   "))
print('\t',validpid("\npid:0123456789   "))


#dict1 = {"byr":"yes","iyr":"yup"}
#string = "My String"
#print(string[0:4])
#print(string[4+1:-1])
#print(dict1)
#print(len(dict1))
#print(("byr" in dict1))
#print(("yes" in dict1))

f = open("day4input.txt")
data = f.readlines()
f.close()

start = 0
lines = ['d']
while(lines != []):
    (lines, start) = extractfrom(data, start)
    acceptable = True
    tmp = ''.join(lines)
    if(validdata(tmp)):
        valid += 1
        #print()
        #print(tmp)
    #for entry in entries:
    #    if entry not in tmp:
#            print(lines,"doesn't have",entry)
    #        acceptable = False
    #if(acceptable):
    #    valid += 1
#        print("Success:",lines,sep='\n')
#    print()
#    print(tmp)
#    data = snip(data)
    print(tmp)

print("Last tmp:",tmp)
print("Last lines: ",lines)
print(valid)
# extract up to first empty line


# check if extraction is valid


# part 2: 132 is too high, 86 is wrong

