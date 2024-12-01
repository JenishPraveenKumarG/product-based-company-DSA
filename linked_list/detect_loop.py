class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next



def detect_loop(head):
    seen = set()
    temp = head

    while temp:
        if temp in seen:
            return True
        temp = temp.next
        seen.add(temp)
    
    return False

    # TC - O(n) + O(1) avg case for inserting element in set + O(1) avg case for searching element in set
    # SC - O(n)

def detect_loops_optimal(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

    # TC - O(n)
    # SC - O(1)

def print_(head):
    visited = set() 
    ans = ""
    temp = head

    while temp:
        if temp in visited:  
            break
        ans += str(temp.data) + " --> "
        visited.add(temp)
        temp = temp.next

    print(ans.rstrip(" --> "))

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    print_(head)
    print(detect_loop(head))
    print(detect_loops_optimal(head))
