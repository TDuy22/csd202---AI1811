class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def addToHead(self, x):
        newNode = Node(x)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode.next

    def addToTail(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

    def addAfter(self, p, x):
        newNode = Node(x)
        currentNode = self.head
        position = 0
        if p == 0:
            self.addToHead(x)
        else:
            while currentNode != None and position != p -1:
                position += 1
                currentNode = currentNode.next

            if currentNode != None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Index not present")

    def traverse(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next
    
    def deleteFromHead(self):
        self.head = self.head.next

    def deleteFromTail(self):
        currentNode = self.head
        while currentNode != None:
            beforeNode = currentNode
            currentNode = currentNode.next

currentNode = Node(5)
beforeNode = currentNode
beforeNode.data = 9
print(currentNode.data)