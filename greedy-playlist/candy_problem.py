def candy(arr):
    n = len(arr)
    left = [-1]*n
    right = [-1]*n
    left[0] = 1
    right[n-1] = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            left[i] = left[i-1] + 1
        else:
            left[i] = 1
    
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            right[i] = right[i+1] + 1
        else:
            right[i] = 1
        
    print(right, left)

    ans = 0
    for i in range(n):
        ans += max(left[i],right[i])
    
    return ans


arr = [0,2,4,3,2,1,1,3,5,6,4,0,0]
arr1 = [1,2,3]
arr2 = [1,3,2,1]

print(candy(arr))

# Tc - O(3n)
# SC - O(2n)


# better solution

def candy(arr):
    n = len(arr)
    left = [-1]*n
    left[0] = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            left[i] = left[i-1] + 1
        else:
            left[i] = 1

    cur = 1
    right = 1
    ans = max(left[n-1],1)
    
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            cur = right + 1
        else:
            cur = 1
        right = cur
        ans += max(left[i],cur)
    
    return ans


arr = [0,2,4,3,2,1,1,3,5,6,4,0,0]
arr1 = [1,2,3]
arr2 = [1,3,2,1]

print(candy(arr))

# Tc - O(3n)
# SC - O(n)

# optimal solution - using slope

def candy(arr):
    n = len(arr)
    if n == 0:
        return 0

    sum_ = 1  # First child gets at least 1 candy
    i = 1

    while i < n:
        if arr[i] == arr[i - 1]:  # Handle equal elements
            sum_ += 1
            i += 1
            continue
        
        # Increasing sequence
        peak = 1
        while i < n and arr[i] > arr[i - 1]:
            peak += 1
            sum_ += peak
            i += 1

        # Decreasing sequence
        down = 1
        while i < n and arr[i] < arr[i - 1]:
            sum_ += down
            down += 1
            i += 1

        # If the decreasing sequence is longer than the peak, adjust sum
        if down > peak:
            sum_ += down - peak

    return sum_

# Test cases
arr = [0, 2, 4, 3, 2, 1, 1, 3, 5, 6, 4, 0, 0]
arr1 = [1, 2, 3]
arr2 = [1, 3, 2, 1]

print(candy(arr))   # Expected: Correct candy distribution count

# TC - O(n)
# SC - O(1)