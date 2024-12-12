''' Fist in First out

operations

    push() - 
    pop()
    top()
    size()
    
    '''

class Queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.queue = []
    
    def push(self,val):
        if len(self.queue) == self.max_size:
            self.pop()
        self.queue.append(val)

    def pop(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        else:
            return None
    
    def top(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        return None
    
    def size(self):
        return len(self.queue)
    
    def print_(self):
        return self.queue


s = Queue(4)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.print_())
print(s.pop())
print(s.print_())
print(s.top())