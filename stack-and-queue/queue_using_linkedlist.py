class Node:
    def __init__(self,data,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail= new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        if self.head is None:
            return
                
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return data

    def top(self):
        if self.head is None:
            return
        else:
            return self.head.data

    def length(self):
        if self.head is None:
            return
        itr = 0
        temp = self.head

        while temp:
            itr +=1
            temp = temp.next
        
        return itr

    def print_(self):
        ans = []
        temp = self.head
        while temp:
            ans.append(temp.data)
            temp = temp.next

        return ans
    

s = Queue()
s.push(10)
s.push(20)
s.push(30)
print(s.print_())
print(s.pop())
print(s.print_())
print(s.length())