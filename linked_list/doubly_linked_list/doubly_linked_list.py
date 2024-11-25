class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, None, None)
            self.head = node
            
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None,None)
            self.head = node
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None,itr)
    
    def print_from_beg(self):
        if self.head is None:
            raise Exception("List is empty")

        ans = ''
        itr = self.head

        while itr:
            ans += str(itr.data) + "-->"
            itr = itr.next
        
        print(ans)

    def print_from_end(self):
        if self.head is None:
            raise Exception("List is empty")
        
        last_node = self.get_last_node()
        
        itr = last_node
        ans = ''

        while itr:
            ans += str(itr.data) + '-->'
            itr = itr.prev
        
        print(ans.rstrip(' --> '))


    
    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next
        
        return itr
    

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            itr = itr.next
            count += 1
            
        return count

    def insert_at_index(self,idx,data):
        if idx < 0 or self.get_length() < idx:
            raise Exception('Invalid Index')
    
        if idx == 0:
            self.insert_at_begining(data)
            return
        
        cnt = 0
        itr = self.head

        while itr:
            if cnt == idx - 1:
                node = Node(data,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            cnt+=1
            itr = itr.next
        return 

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count+=1


if __name__ == '__main__':
    d1 = DoubleLinkedList()
    d1.insert_at_begining(10)
    d1.insert_at_begining(20)
    d1.print_from_beg()
    d1.print_from_end()
    d1.insert_at_end(30)
    d1.print_from_beg()
    d1.insert_at_index(0,5)
    d1.print_from_beg()
    d1.remove_at(0)
    d1.print_from_beg()

    