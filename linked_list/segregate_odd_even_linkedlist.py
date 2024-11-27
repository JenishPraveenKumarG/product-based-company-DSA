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


    
    def segregate(self):
        ans = []
        temp = self.head

        while temp and temp.next:
            ans.append(temp.data)
            temp = temp.next.next

        temp = self.head.next

        while temp and temp.next:
            ans.append(temp.data)
            temp = temp.next.next
        
        if temp:
            ans.append(temp.data)
        
        print(ans)

        idx = 0
        temp = self.head

        while temp:
            temp.data = ans[idx]
            temp = temp.next
            idx += 1
        # TC - O(2n)   SC - O(n) to save the values and print

    
    '''we need to reduce the space complexity'''

    def segregate_(self):

        if self.head is None or self.head.next is None:
        # No need to segregate if the list is empty or has only one node
            return
    
        odd = self.head  # Pointer for odd index nodes
        even = self.head.next  # Pointer for even index nodes
        evenHead = even  # Save the head of the even list

        while even is not None and even.next is not None:
            odd.next = even.next  # Link the next odd node
            odd = odd.next  # Move odd pointer forward
        
            even.next = odd.next  # Link the next even node
            even = even.next  # Move even pointer forward

   
        odd.next = evenHead

        # TC - O(n)
        # SC - O(odd + even)

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_elements_at_beg(6)
    l1.insert_elements_at_beg(5)
    l1.insert_elements_at_beg(1)
    l1.insert_elements_at_beg(4)
    l1.insert_elements_at_beg(3)
    l1.insert_elements_at_beg(2)
    l1.print_()
    l1.segregate_()
    l1.print_()