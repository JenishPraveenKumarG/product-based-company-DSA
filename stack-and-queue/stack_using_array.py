''' Follows first in last out 


operations include

    push() - stack.append(val)
    pop()  - stack.pop()
    top()  - return stack[-1]
    size() - len(stack)
    
'''


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
    
    def size(self):
        return len(self.stack)
    
    def print_(self):
        return self.stack


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.print_())
print(s.pop())
print(s.print_())
print(s.top())