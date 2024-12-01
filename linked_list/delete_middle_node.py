class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def delete_middle_node(head):

    if head is None or head.next is None:
        return 
    
    n = 0
    temp = head

    while temp:
        n += 1
        temp = temp.next
    
    middle = n//2
    print(middle,n)
    cnt = 0
    temp = head
    while temp:
        cnt+=1
        if cnt == middle:
            temp.next = temp.next.next
            break
        temp = temp.next

    return temp
    # TC - O(n) + O(middle)

def delete_middle_node_optimal(head):

    if head is None or head.next is None:
        return

    slow = head
    fast = head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = slow.next.next
    return head
    
    # TC - O(n//2)
    # Sc - O(1) 


def print_(head):
    ans = ""
    temp = head

    while temp:
        ans += str(temp.data) + '-->'
        temp = temp.next
    print(ans.rstrip('-->'))

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    #head.next.next.next.next.next = Node(6)
    print_(head)
    #delete_middle_node(head)
    #print_(head)

    delete_middle_node_optimal(head)
    print_(head)
