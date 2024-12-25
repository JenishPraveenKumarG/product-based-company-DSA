def collision(arr):
    n = len(arr)
    stack = []
    for i in range(n):
        if arr[i] > 0:
            stack.append(arr[i])
        else:
            while stack and stack[-1] < abs(arr[i]):
                stack.pop()
            if not stack or stack[-1]<0:
                stack.append(arr[i])
            elif stack and stack[-1] == abs(arr[i]):
                stack.pop()
    return stack
            

arr = [4,7,1,1,2,-3,-7,17,15,-16]
print(collision(arr))

# TC - O(2n)
# SC - O(n)