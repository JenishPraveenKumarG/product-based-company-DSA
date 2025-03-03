class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    
    def iter_postorder_using_2_stacks(self,root):
        ans = []
        if not root:
            return ans
        
        stack1, stack2 = [],[]
        stack1.append(root)
        while stack1:
            val = stack1.pop()
            stack2.append(val)
            if val.left:
                stack1.append(val.left)
            if val.right:
                stack1.append(val.right)
        
        while stack2:
            val = stack2.pop()
            ans.append(val.data)
        
        return ans    

    def iter_postorder_using_1_stack(self,root):
        stack = []
        ans = []
        cur = root

        while cur or len(stack)!=0:
            if cur:
                stack.append(cur)
                cur = cur.left

            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    ans.append(temp.data)
                    while len(stack)!=0 and temp == stack[-1].right:
                        temp = stack.pop()
                        ans.append(temp.data)
                else:
                    cur = temp
        return ans


    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    sol = Solution()

    res = sol.iter_postorder_using_2_stacks(root)
    res2 = sol.iter_postorder_using_1_stack(root)
    print(res)
    print(res2)


