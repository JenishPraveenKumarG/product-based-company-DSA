class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
    def __lt__(self, other):
        return self.data < other.data


def convert_arr_to_ll(arr):
    head = Node(arr[0])
    temp = head

    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    
    return head

def merge_k_ll(ll_list):
    arr = []
    
    for temp in ll_list:
        while temp:
            arr.append(temp.data)
            temp = temp.next
    
    arr.sort()
    
    merged_ll = convert_arr_to_ll(arr)

    return merged_ll

    # TC - O(number of elements) + O( sorting - nlogn) + O(number of elements)
    # SC - O(number of elements to save the answer)

def merge2(head1, head2):
    
    ans = Node(-1)
    temp = ans

    while head1 and head2:
        if head1.data <= head2.data:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        
        else:
            temp.next = head2
            temp = temp.next
            head2 = head2.next

    while head1:
        temp.next = head1
        temp = temp.next
        head1 = head1.next

    while head2:
        temp.next = head2
        temp = temp.next
        head2 = head2.next
    
    return ans.next


def optimal_merge_1(ll_list):

    head = ll_list[0]

    for i in range(1,len(ll_list)):
        head = merge2(head,ll_list[i])
    
    return head

    # TC - O(n) x O(n x (n+1))//2 - appox (O(k))
    # SC - O(1)


import queue

def optimal_2(list):
    ''' we will use priority queue'''
    pq = queue.PriorityQueue()

    for node in list:
        if node:
            pq.put((node.data,node))
    
    dummy_node = Node(-1)
    temp = dummy_node

    while not pq.empty():

        _, current_node = pq.get()
        if current_node.next:
            pq.put((current_node.next.data, current_node.next))
        
        temp.next = current_node
        temp = temp.next
    
    return dummy_node.next
    # TC - O(k x log k) log k - to put in pq + O(k x n) runs the while loop + O(2 log k) other work in priority queue
    # SC - O(k) priority queue


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
    data1 = [6,4,2]
    data2 = [5,1]
    data3 = [7,3,1,1]
    data4 = [8]
    head1 = add_elements(data1)
    head2 = add_elements(data2)
    head3 = add_elements(data3)
    head4 = add_elements(data4)
    print_(head1)
    print_(head2)
    print_(head3)
    print_(head4)
    ll_list = [head1, head2, head3, head4]
    #a = merge_k_ll(ll_list)
    #a = optimal_merge_1(ll_list)
    a = optimal_2(ll_list)
    print_(a)