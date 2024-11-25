class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # printing elements in forward

    def print_forward(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        dllstr = ''

        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next

        print(dllstr)


    # getting last node in a doubly linked list

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
        

    # printing elements in backward

    def print_backwars(self):
        if self.head is None:
            print('No elemenets in doublylinkedlist')

        last_node = self.get_last_node()
        itr = last_node
        dllback = ''

        while itr:
            dllback += str(itr.data) +'-->'
            itr = itr.prev

        print(dllback)

    # inserting in the begining

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
            
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    # insert at the end 

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)



    # find the length of dll

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            itr = itr.next
            count += 1
            
        return count


    # insert at given index

    def insert_at(self , index , val):
        if index <0 or index > ll.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_begining(val)
            return

        count = 0
        itr  = self.head

        while itr:
            if count == index - 1:
                node = Node(val , itr.next , itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    # removing at user given index

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

    # add ling list of values

    def add_list(self, data_list):
        self.head = Node
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_end(100)
    ll.insert_at_end(101)
    ll.insert_at(1 , 22)
    ll.remove_at(1)
    ll.add_list([1,2])
    ll.print_forward()