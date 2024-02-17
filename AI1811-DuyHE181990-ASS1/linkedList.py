class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head = None):
        self.head = head
    
    def isEmpty(self):
        return (self.head == None)
    
    def addToHead(self, node):
        if self.isEmpty:
            self.head = node
        else:
            node.next = self.head
            self.head = node
