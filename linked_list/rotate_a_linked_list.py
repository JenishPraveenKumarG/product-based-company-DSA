class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


def find_length_ll(head):
    itr = head
    cnt = 0

    while itr:
        cnt+=1
        itr = itr.next
    
    return cnt

def rotate_ll_brute(head,k):
    if head == None or head.next == None:
        return head
    
    for i in range(k):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        end = temp.next
        temp.next = None
        end.next = head
        head = end
    return head

    # TC - O(n x k)


def rotate_ll(head,k):
    n = find_length_ll(head)
    print(n)
    k = k%n
    if k == n or k == 0:
        return head

    temp = head
    while temp.next:
        temp = temp.next
    
    # making connection to head
    temp.next = head
    # to locate the tail node
    val = n-k
    cnt = 0

    while cnt!=val:
        cnt += 1
        temp = temp.next
    
    head = temp.next
    temp.next = None


    return head

    # TC - O(n)


    
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
    data = [5,4,3,2,1]
    head = add_elements(data)
    print_(head)
    rotated_head = rotate_ll_brute(head,3)
    print_(rotated_head)
    