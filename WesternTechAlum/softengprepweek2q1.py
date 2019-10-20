#queue q 1

class Queue:
    def __init__(self, arrSize):
        self.arrSize = arrSize
        self.arr = []
    
    def enqueue(self, val):
        if len(self.arr) == 0 or len(self.arr[0]) == 3:
            newArr = []
            newArr.append(val)
            if(len(self.arr) > 0):
                self.arr.insert(0,newArr)
            else:
                self.arr.insert(0, newArr)
        elif len(self.arr[0]) < 3:
            self.arr[0].insert(0,val)

    def poll(self):

        if len(self.arr) >= 1:
            if len(self.arr[len(self.arr)-1])  ==  0:
                self.arr.pop()
            print(self.arr)

            return self.arr[len(self.arr)-1].pop(len(self.arr[len(self.arr)-1])-1)
        raise Exception("cannot remove item from empty queue")

testQueue = Queue(3)
testQueue.enqueue(1)
testQueue.enqueue(2)
testQueue.enqueue(3)
testQueue.enqueue(4)
print(testQueue.poll())
print(testQueue.poll())
print(testQueue.poll())
print(testQueue.poll())



# calculator question 2
# given a string that represents an expression, return teh result of the expression
# guarantees:
# the only mathematical operators will be + and  *
#all nums will be positive single digit numbers ( 0 - 9)
# each pair of parentheses will eiyher have two numbers and a single operator or a single number

#encounter a closing bracket, pop until opening bracket, 
# perform the past three operations and add it back onto the stack


def calculator(str):
    stack = []
    result = 0
    currEl = ''
    op1 = None
    op2 = None
    op = None

    for char in str:
        if char == ")":
            currEl = stack.pop()
            while currEl != '(':
                if currEl == '*' or currEl == '+':
                    op = currEl
                elif op1 == None:
                    op1 = currEl
                else:
                    op2 = currEl
                currEl = stack.pop()
            if(op != None):
                if(op == '*'):
                    result = int(op1) * int(op2)
                else:
                    result = int(op1) + int(op2) 
                stack.append(result)
                if(len(stack) == 1):
                    return result
                op = None
                op2 = None
            else:
                stack.append(int(op1))
                if(len(stack) == 1):
                    return int(op1)
            op1 = None
        else:
            stack.append(char)

print(calculator('((1+2)*3)'))
print(calculator('(8*((2+4)*2))'))
print(calculator('(((((4)))+1))'))

#q3 implement a LFU cache

#dictionary to keep track of frequency key usage
from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, size):
        self.size = size
        self.nodeKeys = {}
        self.nodeFrequencies = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        if key not in self.nodeKeys:
            return -1
        
        node = self.nodeKeys[key]
        del self.nodeFrequencies[node.count][key]

        if not self.nodeFrequencies[node.count]:
            del self.nodeFrequencies[node.count]
        
        node.count += 1
        self.nodeFrequencies[node.count][key] = node
        
        if not self.nodeFrequencies[self.minCount]:
            self.minCount += 1
            
        return node.val
        
    def put(self, key, value):
        if not self.size:
            return 
        
        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key) 
            return
        
        if len(self.nodeKeys) == self.size:
            k = self.nodeFrequencies[self.minCount].popitem(last=False) 
            del self.nodeKeys[k[0]] 
        
        self.nodeFrequencies[1][key] = self.nodeKeys[key] = Node(key, value, 1)
        self.minCount = 1
        return

cache = LFUCache( 2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))      # returns 1
print(cache.put(3, 3))    #evicts key 2
print(cache.get(2))       #returns -1 (not found)
print(cache.get(3))       # returns 3.
print(cache.put(4, 4))    #evicts key 1.
print(cache.get(1))       #returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))      # returns 4