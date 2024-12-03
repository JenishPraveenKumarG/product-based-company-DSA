class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


def convert_array_to_ll(arr):
    head = Node(-1)
    temp = head

    for i in range(len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return head.next



def merge_brute(head1,head2):
    # store the values of the linked list in array and then sort it and then conver that into linkedlist

    arr = []
    temp = head1

    while temp:
        arr.append(temp.data)
        temp = temp.next
    
    temp = head2

    while temp:
        arr.append(temp.data)
        temp = temp.next
    
    arr.sort()

    new_head = convert_array_to_ll(arr)

    return new_head

    # TC - O(n1 + n2) + O(n logn) + O(n1+n2)


def merge(head1,head2):
    head = Node(-1)
    temp = head

    while head1 and head2:
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        
        else:
            temp.next = head2
            head2 = head2.next
        
        temp = temp.next
    
    while head1:
       temp.next = head1
       head1 = head1.next
    
    while head2:
       temp.next = head2
       head2 = head2.next

    return head.next

    # TC - O(n1 + n2)
    # SC - O(n1 + n2) onlu for storing the answer



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
    data1 = [10,8,4,2]
    data2 = [14,11,6,3,3,1]
    head1 = add_elements(data1)
    head2 = add_elements(data2)
    print_(head1)
    print_(head2)
    ans = merge_brute(head1,head2)
    print_(ans)