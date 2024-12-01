class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def length_of_the_loop(head):
    temp = head
    mpp = {}
    time = 0
    while temp:
        time +=1
        if temp in mpp:
            length = time - mpp[temp]
            return length
        if temp not in mpp:
            mpp[temp] = 0
        mpp[temp] = time
        temp = temp.next
    
    return 0
    
    # TC - O(n) + O(1) for searching element in mpp

def find_length(slow,fast):
    fast = fast.next
    cnt = 1

    while fast!= slow:
        cnt+=1
        fast = fast.next

    return cnt

def length_of_the_loop_optimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return find_length(slow,fast)
    return 0

# TC - O(n)
# SC - O(1)

    
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
    print(length_of_the_loop(head))
    print(length_of_the_loop_optimal(head))
