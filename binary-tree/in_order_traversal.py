class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root,arr):
    if not root:
        return
    
    inOrder(root.left,arr)
    arr.append(root.data)
    inOrder(root.right,arr)


def in_order(root):
    arr = []
    inOrder(root,arr)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = in_order(root)
    print(res)