from Car import *
from Node import *

class Q2_1:
    def f1(self,tree,name, price=-1):
        if name[0] =="B" or price >100: return #kiểm tra thoả mãn đk name và price => kết thúc câu lệnh
        node = Node(Car(name,price)) 
        if tree.isEmpty(): #nếu tree trống add node mới vào root tree
            tree.root = node
            return
        cur = tree.root
        father = None
        while cur: #dừng khi cur = None đến (lá của tree)
            #Tìm vị trí lá tree phù hợp để insert
            if cur.data.Price ==price: 
                # print(f"key {data} is exist ");
                return
            else: 
                father = cur
                if cur.data.Price <price:
                    cur = cur.right
                else:
                    cur = cur.left
        #insert vào tree
        if father.data.Price<price:
            father.right = node    
        else:
            father.left =  node