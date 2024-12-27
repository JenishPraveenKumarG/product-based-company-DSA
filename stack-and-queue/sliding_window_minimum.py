def window_maximum(arr,k):
    ans = []
    n = len(arr)
    for i in range(n-k+1):
        maxi = 0
        for j in range(i,i+k):
            maxi = max(arr[j],maxi)
        ans.append(maxi)
    return ans
arr = [1,3,-1,-1,5,3,2,1,6]
k = 3
print(window_maximum(arr,k))

# TC - O(n-k) x O(k)
# Sc - O(n-k)

# optimal solution

def window_maximum(arr, k):

    from collections import deque

    dq = deque()
    n = len(arr)
    ans = []
    
    for i in range(n):
        
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            ans.append(arr[dq[0]])  # Maximum is at the front of the deque
    
    return ans

# Test the functionarr = [1, 3, -1, -1, 5, 3, 2, 1, 6]
k = 3
print(window_maximum(arr, k))

# TC - O(2n)
# SC - O(k) + O(n-k)