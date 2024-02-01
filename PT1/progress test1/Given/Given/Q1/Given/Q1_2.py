from Car import *
from Node import *
class Q1_2:
    def f2(self, linkList, name="", price=-1):
        node = Node(Car(name,price))
        #if linkList ==None: (Nên đổi thành câu lệnh bên dưới)
        if linkList.isEmpty(): #Kiểm tra xem list có rỗng không
            linkList.head = linkList.tail = node #gán cả đầu và cuối list bằng node mới
        else:
            node.next = linkList.head #nếu list không rỗng thêm node mới vào đầu list
            linkList.head = node
                
