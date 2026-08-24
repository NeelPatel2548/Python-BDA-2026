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

    def delAtFront(self):
        if self.isElement() == True:
            temp = self.head
            if temp.next == None:
                return False
            else:
                self.head = temp.next
        return False

    def delAtEnd(self):
        if self.isElement() == True:
            temp = self.head

            while temp.next.next is not None:
                temp = temp.next

            temp.next = None
        return False

    def delSpecific(self, key):
        if self.isElement() == True:
            temp = self.head

            while temp.next is not None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                temp = temp.next
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
l.insEnd(98)
l.insEnd(300)
l.insEnd(450)

print("Original Linked list: ")
l.display()

#Adding Element at specific position
# key = int(input('Enter key: '))
# l.atSpecific(69, key)

l.delAtFront()
print("Delete First Element: ")
l.display()

l.delAtEnd()
print("Delete Last Element: ")
l.display()

l.delSpecific(98)
print("Delete element 98 :")
l.display()