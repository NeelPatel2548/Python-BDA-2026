#FIFO
class Queue:

    def __init__(self,size):

        self.que = [0] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if(front == -1 and rear == -1):
            front = 0
            return 1
        else:
            return 0
        
    def enqueue(self, data):

        if (self.isEmpty == True):
            print("Queue is Empty")
        else:
            self.rear = self.rear + 1
            self.que[self.rear] = data
            print("Element is: ",self.que[self.rear])
    
    def displayQueue(self):
        print("Front", end=' - ')
        for i in self.que:
            print(i, end=" - ")
        print("Rear")

    

size = 5
qu = Queue(size)

qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)

qu.displayQueue()