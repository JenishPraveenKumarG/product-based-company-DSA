class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# optimal solution

class Solution:
    def checker(self,root1,root2):
        if not root1 or not root2:
            return root1 == root2
        
        return root1.data == root2.data and self.checker(root1.left,root2.left) and self.checker(root1.right,root2.right)
        

# TC - O(n)
# SC - O(n)



if __name__ == "__main__":
    sol = Solution()
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.right.left = Node(4)
    root1.right.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.right.left = Node(4)
    root2.right.right = Node(5)

    res = sol.checker(root1,root2)
    print(res)

