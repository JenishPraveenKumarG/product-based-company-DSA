# naive brute force solution

def minimum(arr):
    mini = float('inf')
    for n in arr:
        if n<mini:
            mini = n
    
    return mini

arr = [4,5,6,7,0,1,2]
print(minimum(arr))

# binary search

def minimum(arr):
    # identify the sorted half
    # sorted half may or maynot have the minimum

    low = 0
    high = len(arr)-1
    mini = float('inf')

    while low <= high:
        mid = (low + high)//2
        if arr[low] <= arr[mid]:
            mini = min(mini,arr[low])
            low = mid + 1
        
        elif arr[low] > arr[mid]:
            mini = min(mini,arr[mid])
            high = mid - 1
        else:
            continue

    return mini

arr = [4,5,6,7,0,1,2]
print(minimum(arr))


# slight optimisation


def minimum(arr):
    # identify the sorted half
    # sorted half may or maynot have the minimum

    low = 0
    high = len(arr)-1
    mini = float('inf')

    while low <= high:
        mid = (low + high)//2

        if arr[low] < arr[high]:
            mini = arr[low]
            break

        if arr[low] <= arr[mid]:
            mini = min(mini,arr[low])
            low = mid + 1
        
        elif arr[low] > arr[mid]:
            mini = min(mini,arr[mid])
            high = mid - 1
        else:
            continue

    return mini

arr = [4,5,6,7,0,1,2]
print(minimum(arr))

# TC - O(log2n)
# SC - O(1)