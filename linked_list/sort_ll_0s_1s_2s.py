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

    def sort_ll(self):
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0

        itr = self.head

        while itr:
            if itr.data == 0:
                cnt_0 += 1
            elif itr.data == 1:
                cnt_1 += 1
            else:
                cnt_2 +=1
            
            itr = itr.next
                
        itr = self.head

        while cnt_0:
            itr.data = 0
            cnt_0 -= 1
            itr = itr.next
        
        while cnt_1:
            itr.data = 1
            cnt_1-=1
            itr = itr.next
        
        while cnt_2:
            itr.data = 2
            cnt_2-=1
            itr = itr.next
        
        # TC - O(2n)
        # SC - O(1)

        '''we were using 2 passes we need to reduce that to one pass and that is the optimal solution'''

        '''we can do this by changing the links'''

    def sort_optimal(self):
        
        zero = one = two = None
        zero_head = zero
        one_head = one
        two_head = two

        itr = self.head
        while itr:
            if itr.data == 0:
                if zero is None:  # If zero list is empty, initialize it
                    zero = itr
                    zero_head = zero
                else:
                    zero.next = itr
                    zero = zero.next
            elif itr.data == 1:
                if one is None:  # If one list is empty, initialize it
                    one = itr
                    one_head = one
                else:
                    one.next = itr
                    one = one.next

            else:
                if two is None:  # If two list is empty, initialize it
                    two = itr
                    two_head = two
                else:
                    two.next = itr
                    two = two.next
            itr = itr.next

            
        if zero:
            zero.next = one_head if one_head else two_head
        if one:
            one.next = two_head
        if two:
            two.next = None

        # Update the head of the sorted list
        self.head = zero_head if zero_head else (one_head if one_head else two_head)
        


    

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_elements_at_beg(1)
    l1.insert_elements_at_beg(2)
    l1.insert_elements_at_beg(0)
    l1.insert_elements_at_beg(2)
    l1.insert_elements_at_beg(1)
    l1.insert_elements_at_beg(0)
    l1.insert_elements_at_beg(1)
    l1.print_()
    #l1.sort_ll()
    l1.sort_optimal()
    l1.print_()
    