class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def postOrder(root,arr):
    if not root:
        return 
    
    postOrder(root.left,arr)
    postOrder(root.right,arr)
    arr.append(root.data)

def post_order(root):
    arr = []
    postOrder(root,arr)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = post_order(root)
    print(res)