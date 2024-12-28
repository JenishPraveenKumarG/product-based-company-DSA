class Stack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')
    
    def push(self,val):
        if val > self.min:
            self.stack.append((val,self.min))
        else:
            self.min = val
            self.stack.append((val,self.min))
    
    def pop(self):
        val = self.stack.pop()
        return val[0]
    
    def get_min(self):
        if len(self.stack) == 0:
            return "Stack is empty"

        return self.stack[-1][1]

    def top(self):
        if len(self.stack) == 0:
            return "Stack is empty"

        return self.stack[-1][0]

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(1)
print(s.top())
print(s.get_min())
print(s.pop())
print(s.top())
print(s.get_min())


print("-------------------------------------")

# TC - O(1)
# SC -- O(2n)

# optimised solution using 1 stack
# 2*val - prev_mini = new_val

class Stackk:
    def __init__(self):
        self.stack = []
        self.min = float('inf') 
    
    def push(self, val):
        if len(self.stack) == 0: 
            self.stack.append(val)
            self.min = val
        else:
            if val > self.min:
                self.stack.append(val)
            else:
                new_val = 2 * val - self.min
                self.stack.append(new_val)
                self.min = val  
    
    def pop(self):
        if len(self.stack) == 0: 
            return "Stack is empty"
        
        x = self.stack.pop()
        if x < self.min:  
            original_min = self.min
            self.min = 2 * self.min - x  
            return original_min
        return x

    def get_min(self):
        if len(self.stack) == 0:  
            return "Stack is empty"
        return self.min  
    
    def top(self):
        if len(self.stack) == 0:  
            return "Stack is empty"
        
        x = self.stack[-1]
        if x < self.min:  
            return self.min
        return x  



s = Stackk()
s.push(10)
s.push(20)
s.push(30)
s.push(1)
print("Top element:", s.top())       
print("Minimum element:", s.get_min())  
print("Popped element:", s.pop())     
print("Top element after pop:", s.top())  
print("Minimum element after pop:", s.get_min())  

# TC - O(n)
# SC - O(n)
