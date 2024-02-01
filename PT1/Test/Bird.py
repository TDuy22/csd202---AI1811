class Bird:
    def __init__(self, type, rate, wing):
        self.type = type
        self.rate = rate
        self.wing = wing
    def __repr__(self):
        return f"({self.type}, {self.rate}, {self.wing})"