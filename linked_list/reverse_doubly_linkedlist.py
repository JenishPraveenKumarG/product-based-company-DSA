# Brute solution

class Node:
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

class Doubly_linked_list:

    def __init__(self):
        self.head = None

    def insert_element_at_begining(self,data):
        if self.head is None:
            node = Node(data,None,None)
            self.head = node
            return
        
        node = Node(data,None,self.head)
        self.head.prev = node
        self.head = node

        return

    def print_dll(self):
        if self.head is None:
            raise Exception("head is empty")

        ans = ''
        itr = self.head

        while itr:
            ans += str(itr.data) + "-->"
            itr = itr.next

        print(ans.rstrip('-->'))

    
    def reverse(self):
        if self.head is None:
            raise Exception("head is empty")
    
        # we will create a stack which has the principle of last in first out LIFO
        # we can pop the most recent element from the stack and place it in the head and next followed by
        
        temp = self.head
        stack = []

        while temp:
            stack.append(temp.data)
            temp = temp.next

        print(stack)

        # again we will assign temp to the top and reverse the values

        temp = self.head
        while temp:
            temp.data = stack.pop()
            temp = temp.next
        
        return

if __name__ == '__main__':
    d1 = Doubly_linked_list()
    d1.insert_element_at_begining(50)
    d1.insert_element_at_begining(40)
    d1.insert_element_at_begining(30)
    d1.insert_element_at_begining(20)
    d1.insert_element_at_begining(10)
    d1.print_dll()
    d1.reverse()
    d1.print_dll()
    d1.reverse_()
    d1.print_dll()

# TC - O(2n)
# SC - O(n)

# Optimal solution

'''we were taking 2 pases now we need to fix this in one pass via swapping the links'''

# we will change the next and prev thats it

    def reverse_(self):
        if self.head is None or self.head.next is None:
            raise Exception("cant reverse")
            # return self.head
        
        temp = None
        current = self.head

        while current:

            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        self.head = temp.prev





