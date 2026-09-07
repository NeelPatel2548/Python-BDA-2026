class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def isElement(self):
        if self.head is None:
            return False
        else:
            return True

    def insBeg(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new          # points to itself
            self.head = new
            return

        # find the last node (its .next currently points to old head)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new.next = self.head
        self.head = new
        temp.next = self.head       # last node now points to new head

    def insEnd(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new
            self.head = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head

    def atSpecific(self, data, key):
        if self.isElement():
            new = Node(data)
            temp = self.head

            while True:
                if temp.data == key:
                    new.next = temp.next
                    temp.next = new
                    return True
                temp = temp.next
                if temp == self.head:      # went all the way around
                    break
            return False
        return False

    def delAtFront(self):
        if self.isElement():
            if self.head.next == self.head:   # only one node
                self.head = None
                return True

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next
            return True
        return False

    def delAtEnd(self):
        if self.isElement():
            if self.head.next == self.head:   # only one node
                self.head = None
                return True

            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head
            return True
        return False

    def delSpecific(self, key):
        if self.isElement():
            if self.head.data == key:
                return self.delAtFront()

            temp = self.head
            while temp.next != self.head:
                if temp.next.data == key:
                    if temp.next == self.head:   # shouldn't hit, guarded above
                        break
                    temp.next = temp.next.next
                    return True
                temp = temp.next
            return False
        return False

    def display(self):
        if self.head is None:
            print(None)
            return

        temp = self.head
        while True:
            print(temp.data, end=" - > ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


l = CircularLinkedList()
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

# Adding Element at specific position
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