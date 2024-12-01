class Node:
    def __init__(self,data,noext = None):
        self.data = data
        self.next = None


def print_(head):
    temp = head

    while temp:
        print(str(temp.data) + "-->", end = "")
    
        temp = temp.next

def find_intersection(head1,head2):
   
    while head2 is not None:
        temp = head1
        while temp:
            if temp == head2:
               return head2
            temp = temp.next

        head2 = head2.next
    
    return None

    # TC - O(n x n)

def better_solution_(head1,head2):
    hashset = set()
    temp = head1
    while temp:
        hashset.add(temp)
        temp = temp.next

    temp = head2
    while temp:
        if temp in hashset:
            return temp
        temp = temp.next
    
    return None

    # TC - O(2n)
    # SC - O(1)

def collisionPoint(head1,head2,d):
    while d:
        head2 = head2.next
        d-=1
    
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next

    return head1
    # or return head2

def optimal_solution_using_length(head1,head2):
    t1 = head1
    n1 = 0
    t2 = head2
    n2 = 0

    while t1:
        n1+=1
        t1 = t1.next
    
    while t2:
        n2+=1
        t2 = t2.next

    if n1 < n2:
        return collisionPoint(head1,head2,n2-n1)
    else:
        return collisionPoint(head2, head1, n1-n2)


    # TC - O(n1) + O(n2) + O(n2-n1) + O(n1)
    # SC - O(1)

def optimal_solution_two_pointers(head1,head2):
    if head1 == None or head2 == None:
        return None
    
    t1 = head1
    t2 = head2

    while t1!=t2:
        t1 = t1.next
        t2 = t2.next

        if t1 == t2:
            return t1

        if t1 == None:
            t1 = head2
        if t2 == None:
            t2 = head1

    # TC - O(n1 + n1)
    # SC - O(1)

if __name__ =="__main__":
    head = Node()