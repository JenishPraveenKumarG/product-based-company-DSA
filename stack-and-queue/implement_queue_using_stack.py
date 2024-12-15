class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,item):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        self.stack1.append(item)

        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    
    def pop(self):
        if len(self.stack1) == 0:
            return "stack is empty"

        return self.stack1.pop()

    def top(self):
        if len(self.stack1) == 0:
            return "stack is empty"
        return self.stack1[-1]

    def print_(self):
        return self.stack1

q = Stack()
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.top())