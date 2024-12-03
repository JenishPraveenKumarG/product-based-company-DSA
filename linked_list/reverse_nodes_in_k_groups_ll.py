class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def reverse_ll(head):
    temp = head
    prev = None
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
    return prev


def func_to_find_kth_node(temp,k):
    k-=1
    while temp is not None and k>0:
        k-=1
        temp = temp.next
    
    return temp

def reverse_k_group(head,k):
    temp = head
    next_node = None
    prev_node = None

    while temp:
        kth_node = func_to_find_kth_node(temp,k)
        if kth_node is None:
            if prev_node:
                prev_node.next = temp
            break
        
        next_node = kth_node.next
        kth_node.next = None
        reverse_ll(temp)

        if temp == head:
            head = kth_node
        else:
            prev_node.next = kth_node
        prev_node = temp
        temp = next_node
    return head
            
    # TC - O(n) for rotating + O(n)for finding the kth node 
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
    data = [10,9,8,7,6,5,4,3,2,1]
    head = add_elements(data)
    print_(head)
    k = 3
    reversed_head = reverse_k_group(head,k)
    print_(reversed_head)