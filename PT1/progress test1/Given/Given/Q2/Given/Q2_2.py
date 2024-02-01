from Car import *
from Node import *

class Q2_2:
    def preOrder(self,p):
        if p==None:
            return
        if (self.check(p.data.Price)):#điều kiện price trong khoảng [3,5]
            self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    def preVisit(self,tree):
        self.preOrder(tree.root)
        print("")
    #end def
    def check(self, x): #check điều kiện chỉ in ra giá trị trong [3,5]
        return x>=3 and x<=5
    def f2(self,tree):
        self.preVisit(tree)