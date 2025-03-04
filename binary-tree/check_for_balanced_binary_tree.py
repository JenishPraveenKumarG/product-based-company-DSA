class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
''' for every node, height(left subtree) - height(right subtree) <= 1 '''

# brute solution

def check_balanced(root):
    if not root:
        return True
    
    left = get_height(root.left)
    right = get_height(root.right)
    
    if abs(left - right) <= 1 and check_balanced(root.right) and check_balanced(root.left):
        return True
    return False

def get_height(root):
    if not root:
        return 0
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return 1 + max(left_height, right_height)

# TC - O(n) x O(n)
# Sc - O(n)

# optimal solution

def optimal_check(root):
    if not root:
        return 0

    left = optimal_check(root.left)
    right = optimal_check(root.right)

    if left == -1 or right == -1:
        return -1
    
    if abs(left - right) > 1:
        return -1
    
    return 1 + max(left,right)

# TC - O(n)
# SC - o(n)
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(6)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.left.right = Node(5)
    root2.left.left.left = Node(6)
    root2.left.left.left.right = Node(8)
    root2.left.left.left.left = Node(7)



    '''res = check_balanced(root)
    print(res)'''

    res = optimal_check(root2)
    if res > 1:
        print(True)
    else:
        print(False)
