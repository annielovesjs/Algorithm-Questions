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

