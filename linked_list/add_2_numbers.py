class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        node = Node(data,self.head)
        self.head = node

    def print_(self):
        ans = ''
        itr = self.head

        while itr:
            ans += str(itr.data) + "-->"
            itr = itr.next

        print(ans.rstrip('-->'))


    def add_(self,l1,l2):
        dummy = Node(0)
        temp = dummy
        carry = 0

        p1 = l1.head
        p2 = l2.head
        
        while p1 or p2:
            sum = 0

            if p1 :
                sum+=p1.data
                p1 = p1.next

            if p2:
                sum+=p2.data
                p2 = p2.next
            
            sum+=carry
            carry = sum//10
            node = Node(sum%10)
            temp.next = node
            temp = temp.next
        
        result = Linked_list()
        result.head = dummy.next
        return result

if __name__ == '__main__':
    l1 = Linked_list()
    l1.insert_at_beg(3)
    l1.insert_at_beg(4)
    l1.insert_at_beg(2)

    l2 = Linked_list()
    l2.insert_at_beg(4)
    l2.insert_at_beg(6)
    l2.insert_at_beg(5)

    l1.print_()
    l2.print_()

    result = l1.add_(l1, l2)

    print("Sum Linked List:")
    result.print_()



