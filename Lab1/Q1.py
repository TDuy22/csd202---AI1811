class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self, head = None):
        self.head = head

    #1
    def addToHead(self, x):
        newNode = Node(x)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode.next
    #2
    def addToTail(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

    #3
    def addAfter(self, p, x):
        newNode = Node(x)
        currentNode = self.head
        position = 0
        if p == 0:
            self.addToHead(x)
        else:
            while currentNode != None and position != p:
                position += 1
                currentNode = currentNode.next

            if currentNode != None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Index not present")

    #4
    def traverse(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
    
    #5
    def deleteFromHead(self):
        if self.head == None:
            print("Link list no data")
            return

        self.head = self.head.next

    #6
    def deleteFromTail(self):
        if self.head == None:
            print("Link list no data")
            return

        currentNode = self.head
        while currentNode != None:
            beforeNode = currentNode
            currentNode = currentNode.next

        beforeNode.next = None

    #7
    def deleteAfter(self, p):
        if self.head == None:
            print("Link list no data")
            return

        currentNode = self.head
        position = 0

        while position != p -1 and currentNode.next != None:
            position += 1
            currentNode = currentNode.next
        
        if currentNode.next != None:
            currentNode.next = currentNode.next.next
        else:
            print("This position doesn't exist")

    #8 del is key word show can decleration function name del change delete
    def delete(self, x):
        currentNode = self.head
        if currentNode == None:
            print("Link list no data")
            return

        while currentNode.next != None:
            if currentNode.next.data == x:
                currentNode.next = currentNode.next.next
                return
        print("Can't founded data")

    #9    
    def search(self, x):
        currentNode = self.head
        while currentNode != None:
            if currentNode.data == x:
                return currentNode
            else:
                return "Can't founded data"

    #10        
    def count(self, x):
        currentNode = self.head
        count = 0
        while currentNode != None:
            count += 1
            currentNode = currentNode.next

        return count
    
    #11
    def delNodeith(self, i):
        currentNode = self.head
        position = 0
        if self.head == None:
            print("Link list no data")
            return

        while currentNode.next != None and position != i -1:
            position += 1
            currentNode = currentNode.next

        if currentNode.next != None:
            currentNode.next = currentNode.next.next
        else:
            print("Can't founded data")

    #12
    def sort(self):
        currentNode = self.head
        newLinkList = singlyLinkedList(self.head)

        while currentNode != Node:
            currentNode = currentNode.next




                




            


        



        
    
    
    
