class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


''' 1. diamter is the longest path between nodes
    2. It need not pass through the root node'''

# brute solution

diamter = 0

def calc_height(root):
    global diamter
    if not root:
        return 0
    left = calc_height(root.left)
    right = calc_height(root.right)

    diamter = max(diamter, left + right)
    return 1+max(left,right)

def diamter_of_binary_tree(root):
    global diamter
    calc_height(root)
    return diamter

# TC - O(n) x O(n)
# SC - O(n)

# optimal solution

def optimal_sol_finding_height(root,diameter):
    if not root:
        return 0
    lh = optimal_sol_finding_height(root.left,diameter)
    rh = optimal_sol_finding_height(root.right,diameter)
    diameter[0] = max(diameter[0],lh+rh)
    return 1+max(lh,rh)

def optimal_solution(root):
    diameter = [0]
    optimal_sol_finding_height(root,diameter)
    return diameter[0]

# TC - O(n)
# Sc - O(n)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.left.left = Node(5)
    root.right.right = Node(6)

    '''res = diamter_of_binary_tree(root)
    print(res)'''

    res = optimal_solution(root)
    print(res)
