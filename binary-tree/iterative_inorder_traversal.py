class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    
    def iter_inorder_traversal(self,root): 
        stack = []
        ans = []
        
        node = root
        while True:
            if node :
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                ans.append(node.data)
                node = node.right
        return ans
        

    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    sol = Solution()

    res = sol.iter_inorder_traversal(root)
    print(res)


