# brute solution

def trapped_rain(arr):
    cnt = 0
    n = len(arr)

    for i in range(n):
        leftmax = 0
        rightmax = 0
        j = i
        while j >= 0:
            leftmax = max(arr[j],leftmax)
            j-=1
        
        j = i
        while j < n:
            rightmax = max(rightmax,arr[j])
            j+=1
        
        cnt+=min(rightmax,leftmax) - arr[i]
    
    return cnt


arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapped_rain(arr))

# TC - O(n x n)
# SC - O(1)


# better solution

# using prefix sum

def trapped_rain(arr):
    cnt = 0
    n = len(arr)

    prefixsum = [0]*n
    suffixsum = [0]*n
    prefixsum[0] = arr[0]


    for i in range(1,n):
        prefixsum[i] = max(prefixsum[i-1],arr[i])
    
    suffixsum[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        suffixsum[i] = max(arr[i],suffixsum[i+1])
    
    for i in range(n):
        left_max = prefixsum[i]
        right_max = suffixsum[i]
        if arr[i] < right_max and arr[i] < left_max:
            cnt += min(left_max,right_max) - arr[i]
    return cnt

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapped_rain(arr))

# TC - O(3n)
# Sc - o(2n)

# optimal approach

def trapped_rain(arr):
    left = 0
    right = len(arr)-1
    total = 0
    left_max = 0
    right_max = 0

    while left <= right:
        if arr[left] < arr[right]:
            if left_max > arr[left]:
                total += left_max - arr[left]
            else:
                left_max = arr[left]
            left+=1
        else:
            if right_max > arr[right]:
                total += right_max - arr[right]
            else:
                right_max = arr[right]
            right-=1
    return total

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapped_rain(arr))

# TC - O(n)
# Sc - O(1)