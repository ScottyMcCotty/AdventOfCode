



from stack_queue import Stack



def decode(line):
    pieces = list(line)
    parts = []
    for piece in pieces:
        if piece != ' ':
            parts += piece
    
#    print(parts)

    stack = Stack()
    for piece in parts:
        if piece.isnumeric():
            previous = stack.peek()
            if previous == None:
                stack.push(piece)
            elif previous == '*':
                stack.pop()
                lastNum = stack.pop()
                stack.push(str(int(lastNum) * int(piece)))
            elif previous == '+':
                stack.pop()
                lastNum = stack.pop()
                stack.push(str(int(lastNum) + int(piece)))
            else:
#                print("Uhh??? Previous was",previous)
                stack.push(piece)
        elif piece == '*' or piece == '+' or piece == '(':
            stack.push(piece)
        elif piece == ')':
            # we know there's a number before
            foundMatch = False
            while(True):
                if stack.peek().isnumeric():
                    num1 = stack.pop()
                    if stack.peek() == '+':
                        stack.pop()
                        num2 = stack.pop()
#                        print(num1,'+',num2)
                        stack.push(str(int(num1) + int(num2)))
                    elif stack.peek() == '*':
                        stack.pop()
                        num2 = stack.pop()
#                        print(num1,'*',num2)
                        stack.push(str(int(num1) * int(num2)))
                    elif stack.peek() == None:
                        # I guess we've reached the bottom of the stack?
#                        print("It is zero? It's",stack.size())
                        stack.push(num1)
                        break
                    elif stack.peek() == '(':
                        # get rid of that damn thing
                        # but we don't want to get rid of others...
                        if not foundMatch:
                            stack.pop()
                            stack.push(num1)
                            foundMatch = True
                        else:
                            stack.push(num1)
                            break
#        print("\nCurrent stack:")
#        stack.printAll()
#        fuckit = input()
#    print("Returning",stack.peek())
#    stack.printAll()
    return int(stack.pop())


f = open("day18.txt")
data = f.readlines()
data = [line.strip() for line in data]

total = 0
for line in data:
    increase = decode(line)
    total += increase
#    print(increase, total)
#    fuckme = input()

print("Total:",total)



# 5047707454315 is too high
# 4940631886147
