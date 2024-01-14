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

    def
