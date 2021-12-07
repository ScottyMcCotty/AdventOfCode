

from stack_queue import Queue
import copy
global turn

def subGame(p1list, p2list, depth):
#    print("In subgame")
    global turn
    p1list = copy.deepcopy(p1list)
    p2list = copy.deepcopy(p2list)
    p1 = Queue()
    p2 = Queue()
    for card in p1list:
        p1.enqueue(card)
    for card in p2list:
        p2.enqueue(card)
    
    previousGame = []
    while p1.size() > 0 and p2.size() > 0:
        turn += 1
        print(turn,depth)
        p1.printAll()
        p2.printAll()
        print()
        for deck in previousGame:
            if deck.compare(p1):
                # winner is p1
#                print("Found a duplicate")
                return True
                
        previousGame += [copy.deepcopy(p1)]
        # check if there's a repeat of previous versions

        p1card = p1.dequeue()
        p2card = p2.dequeue()
        # draw the cards
        
        if p1.size() >= p1card and p2.size() >= p2card:
            if subGame(p1.subQueue(p1card), p2.subQueue(p2card), depth+1):
                p1.enqueue(p1card)
                p1.enqueue(p2card)
            else:
                p2.enqueue(p2card)
                p2.enqueue(p1card)
        else:
            if p1card > p2card:
                p1.enqueue(p1card)
                p1.enqueue(p2card)
            else:
                p2.enqueue(p2card)
                p2.enqueue(p1card)
                
    return p1.size() > p2.size()
                
def doEnd(winner):

    total = 0
    print(winner)
    cardNum = winner.size()
    while winner.size() != 0:
        card = winner.dequeue()
    #    print(card)
        total += cardNum * card
        cardNum -= 1

    print(total)


f = open("day22.in")
data = f.readlines()

data = ''.join(data)
data = data.split('\n')
#print(data)

p1 = Queue()
p2 = Queue()

ii = 1
while data[ii] != '':
    p1.enqueue(int(data[ii]))
    ii += 1

ii += 2
while data[ii] != '':
    p2.enqueue(int(data[ii]))
    ii += 1

turn = 0
winner = ''
previous = []
while p1.size() > 0 and p2.size() > 0:
    turn += 1
    print(turn)
    for deck in previous:
        if deck.compare(p1):
            print("Found duplicate")
            winner = p1
            doEnd(winner)
            break
    previous += [copy.deepcopy(p1)]
    # check if there's a repeat of previous versions

    p1card = p1.dequeue()
    p2card = p2.dequeue()
    # draw the cards

    if p1.size() >= p1card and p2.size() >= p2card:
        if subGame(p1.subQueue(p1card), p2.subQueue(p2card),1):
            p1.enqueue(p1card)
            p1.enqueue(p2card)
        else:
            p2.enqueue(p2card)
            p2.enqueue(p1card)
    else:
        if p1card > p2card:
            p1.enqueue(p1card)
            p1.enqueue(p2card)
        else:
            p2.enqueue(p2card)
            p2.enqueue(p1card)

print("p1 is",p1.size())
print("p2 is",p2.size())

if winner == '':
    if p2.size() > p1.size():
        winner = p2
    else:
        winner = p1

doEnd(winner)

# NOT ANSWER: 33666
# NOT ANSEWR: 32477 (too low)

    
# dad's: 36621
