class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        
    def pop(self):
        if self.head is None:
            return
        else:
            val = self.head.data
            self.head = self.head.next
            return val
    
    def top(self):
        if self.head is None:
            return
        else:
            return self.head.data
    
    def length(self):
        if self.head is None:
            return 0
        else:
            itr = 0
            temp = self.head
            while temp:
                itr += 1
                temp = temp.next
            return itr
    def print_(self):
        ans = []
        temp = self.head
        while temp:
            ans.append(temp.data)
            temp = temp.next
        return ans
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.print_())
print(s.pop())
print(s.print_())
