class Q1_3:
    def f3(self, linkList):
        if self.check(linkList.head.data.Price): #dùng hàm check làm điều kiện kiểm tra price của node đầu
            linkList.head = linkList.head.next
        else:            
            cu = linkList.head
            while(cu.next):
                if (self.check(cu.next.data.Price)):                    
                    break
                cu = cu.next
            if (cu.next==None): 
                return
            else:
                if (cu.next==linkList.tail):
                    linkList.tail=cu    
                cu.next = cu.next.next
              
    def check(self, x):
        #return x==6 #Sai. Điều kiện đề bài là xóa phần tử fisrt node có price bằng 5 nên phải là return x==5
        return x ==5 #Sửa lại câu lệnh trên