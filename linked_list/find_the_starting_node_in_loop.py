class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def loop_starting_node(head):
    seen = set()
    temp = head
    while temp:
        if temp in seen:
            return temp
        seen.add(temp)
        temp = temp.next
    return None
    # TC - O(n) + O(1) avg case for appedning data in set + O(1) avg case for searching data in set
    # TC - O(n)

def loop_starting_node_optimal(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    
    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            return slow
    
    return None

def print__(head):
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
    return


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    print__(head)
    print(loop_starting_node(head))
    print(loop_starting_node_optimal(head))
   
