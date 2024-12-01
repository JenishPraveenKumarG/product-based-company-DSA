class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def insert_at_beginning(head, data):
    for d in data:
        if head is None:
            head = Node(d)
        else:
            node = Node(d, head)
            head.prev = node
            head = node
    return head


def delete_key(head, key):
    temp = head
    while temp:
        if temp.data == key:
            # If node to be deleted is the head node
            if temp == head:
                head = head.next
                if head:  # If there are more nodes
                    head.prev = None
                temp = head  # Move to the next node
                continue
            # Update pointers to remove the node
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
        temp = temp.next
    return head


def print_(head):
    ans = ""
    temp = head
    while temp:
        ans += str(temp.data) + " <-> "
        temp = temp.next
    print(ans.rstrip(" <-> "))


if __name__ == "__main__":
    data = [10, 4, 10, 6, 10, 10]
    head = None
    head = insert_at_beginning(head, data)
    print("Before deletion:")
    print_(head)
    head = delete_key(head, key=10)
    print("After deletion:")
    print_(head)
