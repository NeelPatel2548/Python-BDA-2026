class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# SINGLY LINKED LIST

class LinkedList:

    def __init__(self):
        self.head = None

    # 1. ADD AT HEAD
    def addHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print("Node added at head")

    # 2. ADD AT TAIL
    def addTail(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            print("Node added at tail")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode
        print("Node added at tail")

    # 3. DELETE AT HEAD
    def deleteHead(self):
        if self.head is None:
            print("List is empty")
            return

        print("Deleted:", self.head.data)
        self.head = self.head.next

    # 4. DELETE AT TAIL
    def deleteTail(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print("Deleted:", self.head.data)
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        print("Deleted:", current.next.data)
        current.next = None

    # 5. ADD AFTER GIVEN DATA
    def addAfter(self, target, data):
        current = self.head

        while current is not None:
            if current.data == target:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                print("Node added")
                return

            current = current.next

        print("Element not found")

    # 6. DELETE AFTER GIVEN DATA
    def deleteAfter(self, target):
        current = self.head

        while current is not None:
            if current.data == target:

                if current.next is None:
                    print("No node exists after target")
                    return

                print("Deleted:", current.next.data)
                current.next = current.next.next
                return

            current = current.next

        print("Element not found")

    # 7. SEARCH ELEMENT
    def search(self, key):
        current = self.head
        position = 0

        while current is not None:
            if current.data == key:
                print("Found at position:", position)
                return

            current = current.next
            position += 1

        print("Element not found")

    # DISPLAY
    def display(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# 8. COMMON ELEMENTS IN TWO LINKED LISTS

def commonElements(A, B):
    C = LinkedList()

    current1 = A.head

    while current1 is not None:

        current2 = B.head
        found = False

        while current2 is not None:
            if current1.data == current2.data:
                found = True
                break

            current2 = current2.next

        if found:
            C.addTail(current1.data)

        current1 = current1.next

    return C


# 9. SUM OF LAST N NODES
# ONE TRAVERSAL USING TWO POINTERS

def sumLastN(head, n):

    if n <= 0:
        return 0

    first = head
    second = head
    count = 0
    total = 0

    # Maintain a gap of N nodes
    while count < n:
        if first is None:
            print("Invalid N")
            return None

        first = first.next
        count += 1

    # Move both pointers in one traversal
    # Simultaneously calculate sum
    while first is not None:
        total += second.data
        second = second.next
        first = first.next

    # Include remaining last node
    while second is not None:
        total += second.data
        second = second.next

    return total

# 10. REVERSE LINKED LIST

def reverseList(L):

    previous = None
    current = L.head

    while current is not None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    L.head = previous
    print("List reversed")


# 11. SPLIT ALTERNATE ELEMENTS

def splitList(L):

    A = LinkedList()
    B = LinkedList()

    current = L.head
    position = 0

    while current is not None:

        if position % 2 == 0:
            A.addTail(current.data)
        else:
            B.addTail(current.data)

        position += 1
        current = current.next

    print("First alternate list:")
    A.display()

    print("Second alternate list:")
    B.display()

# 12. CHECK PALINDROME

def palindrome(L):

    if L.head is None:
        return True

    slow = L.head
    fast = L.head
    middlePrev = None

    # Find middle
    while fast is not None and fast.next is not None:
        middlePrev = slow
        slow = slow.next
        fast = fast.next.next

    # For odd number of nodes, skip middle
    secondHalf = slow

    if fast is not None:
        secondHalf = slow.next

    # Reverse second half
    previous = None
    current = secondHalf

    while current is not None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    reversedHead = previous

    # Compare both halves
    first = L.head
    second = reversedHead
    result = True

    while second is not None:
        if first.data != second.data:
            result = False
            break

        first = first.next
        second = second.next

    # Restore second half
    previous = None
    current = reversedHead

    while current is not None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode

    # Reconnect original list
    if fast is not None:
        slow.next = previous
    else:
        middlePrev.next = previous

    return result

# 13. REMOVE DUPLICATES

def removeDuplicates(L):

    current = L.head

    while current is not None:

        runner = current

        while runner.next is not None:

            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    print("Duplicates removed")

# 14. FIND MIDDLE ELEMENT

def findMiddle(L):

    if L.head is None:
        print("List is empty")
        return

    slow = L.head
    fast = L.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    print("Middle element:", slow.data)


# 15. CIRCULAR LINKED LIST
# REMOVE ODD ELEMENTS

class CircularList:

    def __init__(self):
        self.head = None

    def addTail(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = newNode
        newNode.next = self.head

    def removeOdd(self):

        if self.head is None:
            return

        # Remove odd head nodes
        while self.head is not None and self.head.data % 2 != 0:

            if self.head.next == self.head:
                self.head = None
                print("Odd elements removed")
                return

            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        if self.head is None:
            return

        # Remove remaining odd nodes
        current = self.head

        while current.next != self.head:

            if current.next.data % 2 != 0:
                current.next = current.next.next
            else:
                current = current.next

        print("Odd elements removed")

    def display(self):

        if self.head is None:
            print("Circular list is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(HEAD)")

# 16. CYCLE DETECTION

def containsCycle(L):

    slow = L.head
    fast = L.head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def createList():

    L = LinkedList()

    n = int(input("Enter number of elements: "))

    for i in range(n):
        data = int(input("Enter element: "))
        L.addTail(data)

    return L

# MAIN MENU

L = LinkedList()       # SINGLY LINKED LIST
C = CircularList()     # CIRCULAR SINGLY LINKED LIST

while True:


    print("\n--- SINGLY LINKED LIST (SLL) ---")
    print("1.  Add at Head")
    print("2.  Add at Tail")
    print("3.  Delete at Head")
    print("4.  Delete at Tail")
    print("5.  Add After Given Data")
    print("6.  Delete After Given Data")
    print("7.  Search Element")
    print("8.  Display SLL")

    print("\n--- SLL APPLICATIONS ---")
    print("9.  Find Common Elements (Two SLLs)")
    print("10. Sum of Last N Nodes (SLL)")
    print("11. Reverse SLL")
    print("12. Split SLL into Alternate Elements")
    print("13. Check Palindrome (SLL)")
    print("14. Remove Duplicates (SLL)")
    print("15. Find Middle Element (SLL)")
    print("16. Detect Cycle in SLL")

    print("\n--- CIRCULAR SINGLY LINKED LIST (CSLL) ---")
    print("17. Add at Tail (CSLL)")
    print("18. Remove Odd Elements (CSLL)")
    print("19. Display CSLL")

    print("\n--- GENERAL ---")
    print("20. Create New SLL")
    print("0.  Exit")

    choice = int(input("\nEnter choice: "))

    # SINGLY LINKED LIST OPERATIONS

    if choice == 1:
        L.addHead(int(input("Enter data: ")))

    elif choice == 2:
        L.addTail(int(input("Enter data: ")))

    elif choice == 3:
        L.deleteHead()

    elif choice == 4:
        L.deleteTail()

    elif choice == 5:
        target = int(input("Enter target: "))
        data = int(input("Enter new data: "))
        L.addAfter(target, data)

    elif choice == 6:
        target = int(input("Enter target: "))
        L.deleteAfter(target)

    elif choice == 7:
        L.search(int(input("Enter element: ")))

    elif choice == 8:
        print("SINGLY LINKED LIST:")
        L.display()

    # SLL APPLICATIONS

    elif choice == 9:
        print("Create first SLL:")
        A = createList()

        print("Create second SLL:")
        B = createList()

        result = commonElements(A, B)

        print("Common elements (Third SLL):")
        result.display()

    elif choice == 10:
        n = int(input("Enter N: "))
        print("Sum:", sumLastN(L.head, n))

    elif choice == 11:
        reverseList(L)
        print("Reversed SLL:")
        L.display()

    elif choice == 12:
        print("Splitting SLL into alternate elements:")
        splitList(L)

    elif choice == 13:
        if palindrome(L):
            print("SLL is Palindrome")
        else:
            print("SLL is NOT Palindrome")

    elif choice == 14:
        removeDuplicates(L)
        print("SLL after removing duplicates:")
        L.display()

    elif choice == 15:
        findMiddle(L)

    elif choice == 16:
        if containsCycle(L):
            print("Cycle detected in SLL")
        else:
            print("No cycle in SLL")

    # CIRCULAR SINGLY LINKED LIST OPERATIONS

    elif choice == 17:
        C.addTail(int(input("Enter data: ")))

    elif choice == 18:
        C.removeOdd()
        print("CSLL after removing odd elements:")
        C.display()

    elif choice == 19:
        print("CIRCULAR SINGLY LINKED LIST:")
        C.display()

    # CREATE NEW SLL

    elif choice == 20:
        L = createList()
        print("New SLL created:")
        L.display()

    # EXIT

    elif choice == 0:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Try again.")