from Bird import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#end class    
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    #f0    
    def f0():
        return "HE181990"
    
    #f1
    def f1(self, xTpye, xRate, xWing):
        if xTpye[0] == "B" or xRate >10:
            return
        node = Node(Bird(xTpye,xRate,xWing))

        if self.isEmpty():
            self.root = node
            return
        current = self.root
        father = None
        while current:
            if current.data.rate == xRate:
                return #key data exits
            else:
                father = current
                if current.data.rate < xRate:
                    current = current.right
                else:
                    current = current.left
        if father.data.rate< xRate:
            father.right = node
        else:
            father.left = node
    
    #f2
    def preOrder(self,p):
        if p==None:
            return
        if p.data.rate >= 4 and p.data.rate <= 10:
            self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    def visit(self,p):
        if p == None:
            return
        print(f"{p.data}", end = " ")
    def f2(self):
        self.preOrder(self.root)
        print("")

    #f3 
    def f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 1
        while not my.isEmpty():
            p = my.DeQueue()
            if count %2 ==1:
                self.visit(p)
            count+= 1
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("") 

    #f4
    def postOrder(self,p):
        if p == None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        if p.data.wing <=4 and p.data.rates > 6:
            self.visit(p)
    def f4(self):
        self.postOrder(self.root)
        print("")
        
    #f5
    def f5(self):
        self._in_order_filter(self.root)

    def _in_order_filter(self, node):
        if node:
            self._in_order_filter(node.left)
            if node.type[0] == 'A' or node.type[0] == 'C':
                print(f'({node.type},{node.rate},{node.wing})', end=' ')
            self._in_order_filter(node.right)



    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    