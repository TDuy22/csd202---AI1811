class Q1_4:
    def f4(self,linkList):
        if linkList ==None: #kiểm tra nếu linklist trống thì kết thúc function
            return
        i = linkList.head
        while (i.next): #duyệt từ đầu đến cuối list kết thúc khi đến cuối list i.next = None
            j = i.next
            while j:
                #sử dụng thuật toán bubble sort
                if i.data.Price > j.data.Price:
                    t = i.data
                    i.data = j.data
                    j.data = t
                j= j.next
            i = i.next        