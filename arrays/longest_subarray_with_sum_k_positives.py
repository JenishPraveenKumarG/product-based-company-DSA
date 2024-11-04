# Brute

def lon_sub(arr,val):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            s = 0
            for k in range(i,j+1):
                s+=arr[k]
            if s == val:
                ans = max(ans,j-i+1)
    
    return ans
arr = [1,2,3,1,1,1,1,4,2,3]
val = 2
print(lon_sub(arr,val))

# TC - O(n) * O(n) * O(n)
# Sc - O(1)


# better solution

def lon_sub(arr,val):
    n = len(arr)
    ans = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s+=arr[j]
            if s == val:
                ans = max(ans,j-i+1)
    
    return ans
arr = [1,2,3,1,1,1,1,4,2,3]
val = 3
print(lon_sub(arr,val))

# TC - O(n) * O(n)
# SC - O(1)

# better solution using hashing - prefix sum


def lon_sub(arr,val):
    map = {}
    n = len(arr)
    max_len= 0
    sum= 0
    for i in range(n):
        sum += arr[i]
        if sum == val:
            max_len = max(max_len,i+1)
        rem = sum - val
        if rem in map:
            max_len = max(max_len,i-map[rem])

        '''map[sum] = i'''

        # if zeros present means slight change the code so that we can find the longest subarray length
        if sum not in map:
            map[sum] = i
    return max_len
'''arr = [1,2,3,1,1,1,1,4,2,3]
val = 3'''
arr = [2,0,0,0,3]
val = 3
print(lon_sub(arr,val))

# TC - O(n)
# Sc - O(n)


# Optimal solution using sliding window

def lon_sub(arr,val):
    n = len(arr)
    left = 0
    sum = 0
    max_len = 0
    for right in range(n):
        sum += arr[right]
        if sum == val:
            max_len = max(max_len,right-left+1)
        if sum>val:
            sum-=arr[left]
            left+=1
    return max_len

arr = [1,2,3,1,1,1,1,2,2,3]
val = 6
print(lon_sub(arr,val))

# Tc - O(n)
# sc - O(1)