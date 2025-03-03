class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root,arr):
    if not root:
        return
    arr.append(root.data)
    preOrder(root.left,arr)
    preOrder(root.right,arr)

def pre_order(root):
    arr = []
    preOrder(root,arr)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    res = pre_order(root)
    print(res)

# TC - O(n)
# SC - O(n) auxilary space