class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    
    def three_traversals(self,root):
        inorder = []
        preorder = []
        postorder = []
        

        if root is None:
            return []

        stack = [(root,1)]
        while stack:
            node, state = stack.pop()
            if state == 1:
                preorder.append(node.data)
                state = 2
                stack.append((node,state))
                if node.left:
                    stack.append((node.left,1))
            elif state == 2:
                inorder.append(node.data)
                state = 3
                stack.append((node,state))
                if node.right:
                    stack.append((node.right,1))
            else:
                postorder.append(node.data)
            
        return [preorder,postorder,inorder]

        

    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    sol = Solution()

    res = sol.three_traversals(root)
    print(res)


