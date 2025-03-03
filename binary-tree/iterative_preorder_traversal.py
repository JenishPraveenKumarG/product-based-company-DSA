class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    
    def iter_prorder(self,root):
        arr = []
        if not root:
            return arr
        
        stack = []
        stack.append(root)

        while stack:
            val = stack.pop()
            arr.append(val.data)
            if val.right:
                stack.append(val.right)
            if val.left:
                stack.append(val.left)
        return arr
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    sol = Solution()

    res = sol.iter_prorder(root)
    print(res)


