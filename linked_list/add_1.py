class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_ll(head):
    """Reverse a linked list."""
    if head is None or head.next is None:
        return head

    new_head = reverse_ll(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head


def add_1(head):
    """Add 1 to the number represented by the linked list."""
    temp = head
    carry = 1  # Start with carry as 1 to add 1
    while temp:
        temp.data = temp.data + carry
        if temp.data < 10:
            carry = 0
            break
        else:
            temp.data = 0
            carry = 1
        temp = temp.next

    # If carry is still left after traversing the list, add a new node at the beginning
    if carry == 1:
        node = Node(1)
        head = reverse_ll(head)  # Reverse the list to add the new node at the beginning
        node.next = head
        head = node
        return head

    # Otherwise, reverse back and return the result
    head = reverse_ll(head)
    return head


def helper(temp):
    """Recursive helper function to propagate carry."""
    if temp is None:
        return 1  # Initial carry to add 1
    carry = helper(temp.next)
    temp.data = temp.data + carry
    if temp.data < 10:
        return 0  # No carry forward
    temp.data = 0
    return 1  # Carry forward


def add_1_optimal(head):
    """Optimal approach using recursion to add 1."""
    carry = helper(head)
    if carry:
        node = Node(1)
        node.next = head
        head = node
        return node
    return head


def print_(head):
    """Print the linked list."""
    temp = head
    while temp:
        print(f'{temp.data}-->', end="")
        temp = temp.next
    print("None")


# Driver code
if __name__ == "__main__":
    # Test case: Input 999
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)

    print("Original List:")
    print_(head)

    # Test with add_1
    head = reverse_ll(head)  # Reverse the list for addition
    head = add_1(head)
    print("After Adding 1 using add_1:")
    print_(head)

    # Test with add_1_optimal
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)

    print("After Adding 1 using add_1_optimal:")
    head = add_1_optimal(head)
    print_(head)
