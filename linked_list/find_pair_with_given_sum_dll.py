class Node:
    def __init__(self,data,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
def target_sum(head,target):
    temp1 = head
    
    ans = []
    while temp1:
        temp2 = temp1.next
        while temp2 and temp1.data + temp2.data <= target:
            if temp1.data + temp2.data == target:
                ans.append([temp1.data,temp2.data])
                
            temp2 = temp2.next
        temp1 = temp1.next
    
    return ans

    # TC - O(n x n) approx
    # SC - O(ans) only to return it

def target_sum_optimal(head,target):
    temp1 = head
    temp2 = head
    ans = []
    while temp2 and temp2.next:
        temp2 = temp2.next
    

    while temp1.data < temp2.data:
        if temp1.data + temp2.data == target:
            ans.append([temp1.data,temp2.data])
            temp1 = temp1.next
            temp2 = temp2.prev
        
        elif temp1.data + temp2.data > target:
            temp2 = temp2.prev
        
        else:
            temp1 = temp1.next
    
    return ans

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
    
    arr = [1,2,3,4,9]
    head = convert_to_dll(arr)
    print_(head)
    print(target_sum(head,5))
    print(target_sum_optimal(head,5))