import sys
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
        print(None, "\n\n\n")

l = LinkedList()
for i in range(100):
    inp = input("1. insBeg(self, data)\n" \
                "2. insEnd(self, data)\n" \
                "3. InsatSpecific(self, data, key)\n" \
                "4. delAtFront(self)\n" \
                "5. delSpecific(self, key)\n" \
                "6. delAtEnd(self)\n" \
                "7. display(self)\n" \
                "8. Exit\n" \
                "Enter your choice: ")
    match int(inp):
        case 1:
            val = input("Enter Value: ")
            l.insBeg(int(val))

        case 2:
            val = input("Enter Value: ")
            l.insEnd(val)
        case 3:
            key = int(input('Enter key: '))
            val = input("Enter Value: ")
            l.atSpecific(val, key)

        case 4:
            l.delAtFront()
            print("Delete First Element: ")
            l.display()

        case 5:
            l.display()
            val = input("Enter Value you want to delete: ")
            l.delSpecific(val)

        case 6: 
            l.delAtEnd()
            print("Delete Last Element: ")
            l.display()

        case 7:
            l.display()    
            
        case 8:
            sys.exit("Existing............")



    
    
 
        

    


