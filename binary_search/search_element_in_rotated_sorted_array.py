# brute force solution

def search_in_rotated(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [7,8,9,1,2,3,4,5,6]
target = 1

print(search_in_rotated(arr,target))


# TC - O(n) worst case
# SC - O(1)


# optimal solution using binary search

# identify the sorted half

def search_in_rotated(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target and target <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

arr = [7,8,9,1,2,3,4,5,6]
target = 1

print(search_in_rotated(arr,target))


# TC - O(log2n)
# SC - O(1)
    
        
