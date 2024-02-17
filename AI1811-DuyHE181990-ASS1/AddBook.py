from book import *
from linkedList import *
def addBook(database, bookAdd):
    if database.isEmpty:
        database.head = bookAdd
    else:
        currentNode = database.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = bookAdd
