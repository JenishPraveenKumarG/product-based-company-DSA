class Node:
    def __init__(self,data,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

def remove_dulpicate(head):
    temp = head

    while temp and temp.next is not None:
        Next_Node = temp.next

        while Next_Node and Next_Node.data == temp.data:
            Next_Node = Next_Node.next
        
        temp.next = Next_Node
        if Next_Node:
            Next_Node.prev = temp
        
        temp = temp.next
    
    return head

    # TC - O(n) calculate the number of times the loop occurs
    # SC - O(1)


def convert_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1,len(arr)):
        node = Node(arr[i],None,prev)
        prev.next = node
        prev = node
    
    return head


def print_(head):
    ans = ""
    temp = head

    while temp:
        ans += str(temp.data) + "<-->"
        temp = temp.next
    
    print(ans.rstrip('<-->'))

if __name__ == "__main__":
    
    arr = [1,1,1,2,3,3,4]
    head = convert_to_dll(arr)
    print_(head)
    val = remove_dulpicate(head)
    print_(val)
    