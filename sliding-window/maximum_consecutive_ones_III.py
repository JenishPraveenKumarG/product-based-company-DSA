# atmost k flips
def maximum(arr,k):
    '''generate all subarrays with atmost 2 zeros'''

    n = len(arr)
    max_len = 0
    for i in range(n):
        zeros = 0
        for j in range(i,n):
            if arr[j] == 0:
                zeros += 1
            if zeros <= k:
                max_len = max(max_len,j-i+1)
            else:
                break
    return max_len


arr = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(maximum(arr,k))

# TC - O(n x n)
# SC - O(n)

# optimised solution

def maximum(arr,k):
    l = 0
    max_len = 0
    zeros = 0

    for r in range(len(arr)):
        if arr[r] == 0:
            zeros += 1
        
        if zeros > k:
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l+=1
        
        max_len = max(max_len,r-l+1)
    return max_len

arr = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(maximum(arr,k))

# TC - O(n + n)
# Sc - O(1)

# most optimal solution for companies like google

def maximum(arr,k):
    n = len(arr)
    l = 0
    max_len = 0
    zeros = 0

    for r in range(n):
        if arr[r] == 0:
            zeros += 1

        if zeros > k:
            if arr[l] == 0:
                zeros -= 1
            l+=1
        
        if zeros <= k:
            max_len = max(max_len,r-l+1)
        
        
    return max_len


arr = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(maximum(arr,k))

# TC - O(n)
# SC - O(1)