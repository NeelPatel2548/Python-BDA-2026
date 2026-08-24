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

        # print("Inserted")

    def insEnd(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        
        while temp.next is not None:
            temp = temp.next
        
        temp.next = new 

    def atSpecific(self, data, key):
        if self.isElement() == True:
            new = Node(data)
            temp = self.head

            while temp.next is not None:            #if we want to add at one beofre that valye then, ----`         temp.next.data
                if temp.data == key:
                    new.next = temp.next
                    temp.next = new
                    return True
                temp = temp.next
            return False
        return False

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
l.insEnd(45)

l.display()

key = int(input('Enter key: '))
l.atSpecific(69, key)


l.display()