class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        node = Node(data,self.head)
        self.head = node
        return

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        node = Node(data,None)
        itr.next = node
        return
    
    def insert_values_in_linked_list(self,data_list):
        '''to create a new linked list'''
        # so set head as None
        self.head = None

        for data in data_list:
            if self.head is None:
                node = Node(data,None)
                self.head = node
            else:
                self.insert_at_end(data)

    def get_length_of_ll(self):
        if self.head is None:
            return -1
        
        itr = self.head
        cnt = 0

        while itr:
            cnt+=1
            itr = itr.next
        
        return cnt

    def remove_at_index(self,idx):
        if idx < 0 or idx >=  self.get_length_of_ll():
            raise Exception('Invalid index')
        
        if idx == 0:
            self.head = self.head.next
            return
        
        cnt = 0
        itr = self.head

        while itr:
            ''' we will identy the index less than the given index and we will give connection to the next element of the index in this way we can remove the element'''
            if cnt == idx - 1:
                itr.next = itr.next.next
                break
            cnt+=1
            itr = itr.next

    def insert_at_index(self,idx,data):
        if idx < 0 or idx >= self.get_length_of_ll():
            raise Exception('Invalid Index')
        
        if idx == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        cnt = 0
        while itr:
            if cnt == idx - 1:
                #node = Node(data,None)
                # node.next = itr.next
                node = Node(data,itr.next)
                itr.next = node
                break
            cnt+=1
            itr = itr.next
        
        return



    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return 
        
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_begining(5)
    l1.insert_at_begining(89)
    l1.insert_at_end(100)
    l1.print()
    l1.insert_values_in_linked_list([1,2,3,4,5,6])
    l1.print()
    print(l1.get_length_of_ll())
    l1.remove_at_index(2)
    l1.print()
    l1.insert_at_index(2,100)
    l1.print()