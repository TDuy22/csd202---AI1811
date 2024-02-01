from Car import *
from Node import *
class Q1_1:
    
    def f1(self, linklist, name="", price=-1):
        if name.startswith("B") or price >100:#kiểm tra điều kiện tên bắt đầu bằng B hoặc price > 100
            return #điều kiện đúng kết thúc function
        n = Node(Car(name,price))
        if (linklist.isEmpty()):
            linklist.head = linklist.tail = n #nếu link list trống thì gán cả đầu và tail của linklist là n
        else:
            linklist.tail.next = n #Linklist không trống => nối phần tử n vào đuôi linklist
            linklist.tail = n    #gán điểm cuối của linklist là n