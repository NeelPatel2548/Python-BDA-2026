class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isElement(self):
        if self.head is None:
            return False
        else:
            return True
        
    def insBeg(self, data):
        new = Node(data)

        new.next = self.head
        self.head = new
  
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" - > ")
            temp = temp.next
        print(None)



l = LinkedList()
l.insBeg(10)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insBeg(50)
l.insBeg(60)
l.insBeg(10)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insBeg(50)
l.insBeg(60)

