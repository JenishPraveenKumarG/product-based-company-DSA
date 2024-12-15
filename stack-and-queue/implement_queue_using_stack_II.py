class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, item):
        # Add the item to stack1
        self.stack1.append(item)
    
    def pop(self):
        # If stack2 is not empty, pop from it
        if len(self.stack2) != 0:
            return self.stack2.pop()

        # Transfer all elements from stack1 to stack2 in reversed order
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        
        # Pop from stack2
        if len(self.stack2) != 0:
            return self.stack2.pop()
        else:
            return "Stack is empty"
    
    def size(self):
        # Return the combined size of stack1 and stack2
        return len(self.stack1) + len(self.stack2)
    
    def top(self):
        # Check stack2 first for the top element
        if len(self.stack2) != 0:
            return self.stack2[-1]
        
        # Transfer elements from stack1 to stack2 to access the top
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        
        if len(self.stack2) != 0:
            return self.stack2[-1]
        else:
            return "Stack is empty"
    
    def print_(self):
        # Return the current state of the simulated queue
        return self.stack1[::-1] + self.stack2

# Example usage
q = Stack()
q.push(10)
q.push(20)
q.push(30)
print(q.top())  # Should print 10 (top of the queue)
print(q.pop())  # Should remove and print 10
print(q.top())  # Should print 20 (new top after pop)
print(q.size())  # Should print 2 (remaining items)
print(q.print_())  # Should print the queue's state
