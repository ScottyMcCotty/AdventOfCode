

def checkAdj( num ):
    digits = str(num)
    for ii in range(len(digits)-1):
        if(digits[ii] == digits[ii+1]):
            return True
    return False

def checkOrder( num ):
    digits = str(num)
    for ii in range(len(digits)-1):
        if(digits[ii+1] < digits[ii]):
            return False
    return True

def checkNoThree( num ):
    digits = str(num)
    for ii in range(len(digits)-2):
        if(digits[ii] == digits[ii+1] and digits[ii] == digits[ii+2]):
            return False
    return True

def checkValid( num ):
    return (checkAdj(num) and checkOrder(num) and checkNoThree(num))

print(checkValid(122345))
print(checkValid(123456))
print(checkValid(111233))
print(checkValid(123455))
print(checkValid(123444))
print(checkValid(444555))

# my range: 367479-893698
start = 367479
end = 893698
ii = start
valid = 0
while(ii < end):
    if( checkValid(ii) ):
        valid += 1
    ii += 1
print(valid)
