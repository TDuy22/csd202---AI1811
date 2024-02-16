class book:
    def __init__(self, bid = None, title = None, author = None, status = None):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
    
class borrowerBook:
    def __init__(self, bid = None, borrower = None):
        self.bid = bid
        self.borrower = borrower

