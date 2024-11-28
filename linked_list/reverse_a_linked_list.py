class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_elements_at_beg(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        node = Node(data,self.head)
        self.head = node
    
    def print_(self):
        ans = ''
        if self.head is None:
            raise Exception("linked list is Empty")
        
        itr = self.head

        while itr:
            ans += str(itr.data) + '-->'
            itr = itr.next
        
        print(ans.rstrip('-->'))

    def reverse(self):
        stack = []
        itr = self.head

        while itr:
            stack.append(itr.data)
            itr = itr.next
        
        temp = self.head

        while temp:
            temp.data = stack.pop()
            temp = temp.next
        
        return
    
    # TC - O(2n)
    # SC - O(n) stack

    def reverse_optimal(self):
        temp = self.head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        self.head = prev

    def reverse_optimal_2_using_recursion(head):

        if head is None or head.next is None:
            return head
        
        new_head = reverse_optimal_2_using_recursion(head.next)
        front = head.next
        front.next = head
        head.next = None

        return new_head



    
    

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_elements_at_beg(5)
    l1.insert_elements_at_beg(4)
    l1.insert_elements_at_beg(3)
    l1.insert_elements_at_beg(2)
    l1.insert_elements_at_beg(1)
    l1.print_()
    #l1.remove_nth_node_from_back(1)
    l1.reverse()
    l1.print_()
    l1.reverse_optimal()
    l1.print_()
    l1.reverse_optimal_2_using_recursion()
    l1.print_()