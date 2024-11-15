# contains duplicates

def search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        
        if arr[low] == arr[mid] and arr[high] == arr[high]:
            low += 1
            high -=1
            continue
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


arr = [7,8,1,2,3,3,3,4,5,6]
target = 3

print(search(arr,target))
# we must say yes or no

# TC - o(log2n)
# worst case near about O(n//2)

# SC - O(1)