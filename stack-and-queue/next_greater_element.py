# monotonic stack - we will store data in specific format in the stack

# brute solution

def next_greater(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(i,n):
            if arr[j] > arr[i]:
                ans.append(arr[j])
                flag= 1
                break
        if flag == 0:
            ans.append(-1)

    return ans

arr = [6,0,8,1,3]
print(next_greater(arr))

# TC - O(n**2)
# Sc - O(n) to store the answer

# using stack optimsed one...... iterating from the back



def next_greater(arr):
    # we will store the values in decreasing order

    stack = []
    n = len(arr)
    ans = [-1]*n
    for i in range(n-1,-1,-1):
        while len(stack)!=0 and stack[-1] < arr[i]:
            stack.pop()
        
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        
        stack.append(arr[i])

    return ans

arr = [4,12,5,3,1,2,5,3,1,2,4,6]
print(next_greater(arr))

# TC - O(2n)
# SC - O(n)