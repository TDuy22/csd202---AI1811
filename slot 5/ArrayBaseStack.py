class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    def push(self, e):
        self.data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()

def is_matched(expr):
    lefty = "({["
    righty = "]})"
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                returnFalse
        return S.is_empty()

def is_matched_html(raw)
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty