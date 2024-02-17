from book import *
from linkedList import*
def viewBook(database):
    print("Bid".ljust(7, " ") +"| "+"Title".ljust(15, " ") +"| "+ "Author".ljust(30, " ") + "| " + "status")
    print("-"*60)

    currentNode = database.head
    while currentNode != None:
        print(currentNode.bid.ljust(7, " ") +"| "+currentNode.title.ljust(15, " ") +"| "+ currentNode.author.ljust(30, " ") + "| " + currentNode.status)