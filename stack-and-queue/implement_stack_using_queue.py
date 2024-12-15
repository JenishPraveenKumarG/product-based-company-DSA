from collections import  deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self,item):
        n = self.size()
        self.queue.append(item)
        for _ in range(n):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if len(self.queue) == 0:
            raise IndexError
    
        return self.queue.popleft()
    
    def top(self):
        if len(self.queue) == 0:
            raise IndexError
    
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    

stack = Queue()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack.top())
print(stack.pop())
print(stack.top())

stack.pop()
print(stack.pop())
