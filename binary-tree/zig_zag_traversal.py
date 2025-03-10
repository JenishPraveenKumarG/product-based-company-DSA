class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def traversal(self,root):
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)
        leftToRight = True

        while q:
            n = len(q)
            row = [0] * n

            for i in range(n):
                node = q.popleft()
                index = i if leftToRight else n-1-i
                row[index] = node.data

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            leftToRight = not leftToRight
            result.append(row)

        return result

# TC - O(n)
# SC - O(n)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(6)

    res = Solution().traversal(root)
    print(res)