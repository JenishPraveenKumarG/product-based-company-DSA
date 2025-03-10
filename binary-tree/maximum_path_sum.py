class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# optimal solution

def find_max_path_sum(root,maxi):
    if not root:
        return 0
    leftMaxPath = max(0,find_max_path_sum(root.left,maxi))
    rightMaxPath = max(0,find_max_path_sum(root.right,maxi))
    maxi[0] = max(maxi[0],leftMaxPath + rightMaxPath + root.data)

    return max(leftMaxPath, rightMaxPath) + root.data

def maximum_path_opt(root):
    '''try out all possible path and find the maximum path sum'''
    maxi = [float('-inf')]
    find_max_path_sum(root,maxi)
    return maxi[0]

# TC - O(n)
# Sc - O(n)

if __name__ == "__main__":
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(15)
    root.right.left = Node(7)
    root.right.right = Node(20)

    res = maximum_path_opt(root)
    print(res)

