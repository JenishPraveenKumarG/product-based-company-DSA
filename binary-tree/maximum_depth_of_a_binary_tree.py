class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1+max(left,right) 

    # TC - O(n)
    # SC - O(n)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.left = Node(5)
    root.right.right = Node(6)

    res = max_depth(root)
    print(res)
