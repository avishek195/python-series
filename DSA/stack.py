

class Stack:
    def __init__(self):
        self.stack = []
        self.MAX_LENGTH = 5
        self.top = -1

    def push(self,data):
        if self.top >= self.MAX_LENGTH - 1:
            print("Stack is full")
            return
        self.top += 1
        self.stack.append(data)
        

    def pop(self):
        if self.top < 0:
            print("Stack is empty")
            return
        del self.stack[self.top]
        self.top -= 1

    def peek(self):
        if self.top < 0:
            print("Stack is empty")
            return []
        return self.stack[self.top]

    def getValues(self):
        if self.top == -1:
            print("Stack is empty")
            return []
        for value in self.stack:
            print(value ,end=" ")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()


# s.getValues()
print(s.peek())