

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def peekpeek(self):
        if len(self.stack) < 2:
            return None
        return self.stack[-2]

    def printAll(self):
        ii = len(self.stack)-1
        while ii >= 0:
            print(self.stack[ii])
            ii -= 1

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def compare(self, other):
        if self.size() != other.size():
            return False
        for ii in range(len(self.queue)):
            if self.queue[ii] != other.queue[ii]:
                return False
        return True

    def subQueue(self, length):
        return self.queue[0:length]

    def printAll(self):
        print(self.queue)
