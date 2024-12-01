class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next



def middle_element(head):
    n = 0
    temp = head
    while temp:
        n+=1
        temp = temp.next

    middle = (n//2) + 1
    c = 0
    temp = head

    '''while middle != 1:
        middle -= 1
        temp = temp.next'''
    
    while temp:
        middle-=1
        if middle == 0:
            break
        temp = temp.next
    
    print(temp.data)
    return

    # TC - O(n) + O(n//2)

def middle_element_optimal(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    print(slow.data)
    return

    # TC - O(n//2)

def print_(head):
    ans = ""
    temp = head

    while temp:
        ans+=str(temp.data) + "-->"
        temp = temp.next
    
    print(ans.rstrip("-->"))

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print_(head)
    middle_element(head)
    middle_element_optimal(head)
