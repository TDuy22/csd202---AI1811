class arrayStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def clear(self):
        self.stack == []

    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("stack empty")
        else:
            x = self.stack[len(self.stack)-1]
            self.stack.pop()
            return x
    
    def top(self):
        if not self.isEmpty:
            return self.stack[-1]
        else:
            raise Exception("Empty stack")
        
    def traverse(self):
        for i in range(len(self.stack) -1, -1, -1):
            print(self.stack[i])

def decimalToBinary(decimal):
    stack = arrayStack()
    x = decimal
    x = int(x)

    while not x == 0:
        r = x %2
        x = x//2
        stack.push(r)
        
    binary = ''
    while not stack.isEmpty():
        binary += str(stack.pop())
    print(binary)
