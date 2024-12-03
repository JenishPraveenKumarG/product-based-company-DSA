class Node:
    def __init__(self, data=None, nextNode=None, childNode=None):
        self.data = data
        self.next = nextNode
        self.child = childNode


def convert(arr):
    if len(arr) == 0:
        return None
    
    head = Node(arr[0])
    temp = head

    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        temp.child = new_node
        temp = temp.child
    
    return head


def flattened_linked_list(head):
    # iterate and store the values in a array and then convert it into linkedlist
    arr = []
    temp = head

    while temp:
        t2 = temp

        while t2:
            arr.append(t2.data)
            t2 = t2.child
        
        temp = temp.next
    
    arr.sort()
    return convert(arr)

    # TC - O(n x m) + O(nlogn) + (n x m)
    # SC - O(n x m) * 2

def merge(head1,head2):
    dummy_node = Node(-1)
    res = dummy_node

    while head1 and head2:
        if head1.data <= head2.data:
            res.child = head1
            res = head1
            head1 = head1.child
        
        else:
            res.child = head2
            res = head2
            head2 = head2.child

        res.next = None

    
    if head1:
        res.child = head1
        res = head1
    else:
        res.child = head2
        res = head2

    # Break the last node's
    # link to prevent cycles
    if dummy_node.child:
        dummy_node.child.next = None

    return dummy_node.child

def flatten_optimal(head):
    if head == None or head.next is None:
        return head

    merge_head = flattened_linked_list(head.next)
    head = merge(head,merge_head)

    return head

    # TC - O(n1 + n2) it is time for merge and then O(n+m) for traversal



def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()


def printOriginalLinkedList(head, depth=0):
    while head:
        print(head.data, end="")

        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        if head.next:
            print()
            print("| " * depth, end="")

        head = head.next
    

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)


printOriginalLinkedList(head)
print()
a = flatten_optimal(head)
printLinkedList(a)