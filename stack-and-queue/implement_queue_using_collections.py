from collections import  deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError
    
        return self.queue.popleft()
    
    def peak(self):
        if len(self.queue) == 0:
            raise IndexError
    
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    

a = Queue()
a.enqueue(10)
a.enqueue(20)
print(a.peak())
print(a.dequeue())
print(a.peak())