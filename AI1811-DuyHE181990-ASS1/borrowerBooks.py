class borrowerBooks:
    def __init__(self, bid = None, borrower = None):
        self.bid = bid
        self.borrower = borrower

hi = borrowerBooks("abc", "xyz")
print(hi is borrowerBooks("abc", "xyz"))