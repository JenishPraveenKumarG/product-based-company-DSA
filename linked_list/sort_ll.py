class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def sort_ll(head):
    arr = []
    temp = head

    while temp:
        arr.append(temp.data)
        temp = temp.next

    temp = head
    arr.sort()
    i = 0
    while temp:
        temp.data = arr[i]
        i+=1
        temp = temp.next
    
    return head

    # TC - O(n) + O(nlogn) + O(n)
    # SC - O(n)

def merge(left,right):
    dummy_node = Node(-1)
    temp = dummy_node
    while left and right:
        if left.data <= right.data:
            temp.next = left
            temp = temp.next
            left = left.next
        else:
            temp.next = right
            temp = temp.next
            right = right.next

    while left:
        temp.next = left
        temp = temp.next
        left = left.next
    
    while right:
        temp.next = right
        temp = temp.next
        right = right.next
    
    return dummy_node.next

def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def sort_optimal_merge(head):
    if head is None or head.next is None:
        return head

    middle = find_middle(head)
    left = head
    right = middle.next
    middle.next = None

    left = sort_optimal_merge(left)
    right = sort_optimal_merge(right)

    return merge(left,right)

    # TC - O(logn) + O(n) + O(n//2)
    # SC - O(1)


def add_elements(data):
    head = Node(data[0])

    for i in range(1,len(data)):
        node = Node(data[i],head)
        head = node

    return head

def print_(head):
    ans = ""
    temp = head

    while temp:
        ans += str(temp.data) + "-->"
        temp = temp.next

    print(ans.rstrip("-->"))


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9]
    head = add_elements(data)
    print_(head)
    sorted_head = sort_optimal_merge(head)
    print_(sorted_head)