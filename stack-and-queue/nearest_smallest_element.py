def nearest_small_element(arr):
    n = len(arr)
    nse = [-1]*n
    for i in range(n):
        for j in range(i-1,-1,-1):
            if arr[j] < arr[i]:
                nse[i] = arr[j]
                break
    return nse

arr = [4,5,2,10,8]
print(nearest_small_element(arr))

# TC - O(n x n)
# SC - O(n) to store the answer

def nearest_small_element_(arr):
    stack = []
    n = len(arr)
    ans = []

    for i in range(n):
        while len(stack)!=0 and stack[-1] > arr[i]:
            stack.pop()

        if len(stack) == 0:
            ans.append(-1)
        
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    
    return ans
        

arr = [4,5,2,10,8]
print(nearest_small_element_(arr))

# TC - O(2n)
# SC - O(n) we only use extra space to store the answer
