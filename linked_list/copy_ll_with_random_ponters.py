
class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


# Function to clone the linked list
def cloneLL(head):
    mpp = {}
    temp = head

    while temp:
        new_node = Node(temp.data)
        mpp[temp] = new_node

        temp = temp.next
    
    temp = head
    while temp.next:
        copy_node = mpp[temp]
        copy_node.next = mpp[temp.next]
       
        copy_node.random = mpp[temp.random]
        
        temp = temp.next

    return mpp[head]

    # Tc - O(n) + O(n)
    # SC - O(n) +O(n) tp return the answer

def clone_ll_optimal(head):
    '''insert inbetween'''

    temp = head

    while temp:
        copy_node = Node(temp.data)
        copy_node.next = temp.next
        temp.next = copy_node
        temp = temp.next.next
    
    temp = head

    while temp:
        copy_node = temp.next
        copy_node.random = temp.random.next
        temp = temp.next.next
    
    dummy_node = Node(-1)
    res = dummy_node

    temp = head

    while temp:
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next

    return dummy_node.next




# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head is not None:
        print(f"Data: {head.data}", end="")
        if head.random is not None:
            print(f", Random: {head.random.data}")
        else:
            print(", Random: nullptr")
        head = head.next


# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    #clonedList = cloneLL(head)

    clonedList = clone_ll_optimal(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)
                                
                            