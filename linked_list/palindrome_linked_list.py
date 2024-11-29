class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    

def isPalindrome(head):
    temp = head
    stack = []

    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head

    while temp:
        if temp.data != stack.pop():
            return False
        temp = temp.next
    
    return True
    # TC - O(2n) 
    # SC - O(n)

def reverse_ll(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_ll(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

def is_palindrome_optimal(head):
    # first we will find the middle

    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    new_head = reverse_ll(slow.next)
    first = head
    second = new_head

    while second:
        if first.data != second.data:
            return False
        first = first.next 
        second = second.next

    return True

    # TC - O(n/2 + n/2 + n/2 + n/2) = O(2n)
    # SC - O(1)

def print_(head):
    temp = head
    while temp:
        print(temp.data, "-->",end = " ")
        temp = temp.next
    print()
    

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)
    print_(head)

    if isPalindrome(head):
        print('Palindrome')
    else:
        print("Not a palindrome")
    
    print(is_palindrome_optimal(head))

    