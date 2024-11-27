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

    def remove_nth_node_from_back(self,idx):
        cnt = 0
        temp = self.head

        while temp:
            cnt+=1
            temp = temp.next
        
        prev_node = cnt - idx

        temp = self.head

        if cnt == idx:
            self.head = self.head.next
        
        else:
            # to find the previous node of the node that need to be removed

            res = cnt - idx
            temp = self.head

            while temp:
                res -= 1

                if res == 0:
                    break

                temp = temp.next
            
            temp.next = temp.next.next
        return

        # TC - O(len of ll) + O(len-n) to reach the previous node
        # SC - O(1)

    def remove_optimal_solution(self,idx):
        slow = fast = self.head

        for i in range(idx):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        # TC - O(len of linked list)
        # Sc - O(1)
    
    

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_elements_at_beg(5)
    l1.insert_elements_at_beg(4)
    l1.insert_elements_at_beg(3)
    l1.insert_elements_at_beg(2)
    l1.insert_elements_at_beg(1)
    l1.print_()
    #l1.remove_nth_node_from_back(1)
    l1.remove_optimal_solution(4)
    l1.print_()