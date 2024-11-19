# brute solution

def peak(arr):
    n = len(arr)
    for i in range(n-1):
        if i == 0 :
            if arr[i] > arr[i+1]:
                return arr[i]
            else:
                continue

        if i == n-2:
            if arr[n-1] > arr[n-2]:
                return arr[i]
            else:
                continue
    
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            return arr[i]


arr = [1,2,3,4,5,6,7,8,5,1]
print(peak(arr))

# condition for preak is --->  arr[i-1] < arr[i] > arr[i+1]
# TC - O(n)
# SC - O(1)


def peak(arr):
    low = 0
    high = len(arr)-1

    if arr[low] > arr[low+1]:
        return low
    
    if arr[high] > arr[high-1]:
        return high
    low = 1
    high = len(arr)-2

    while low <= high:
        mid = (low + high)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
            return mid
        
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        
        else:
            high = mid - 1

arr = [1,2,3,4,5,6,7,8,5,1]
print(peak(arr))

# TC - O(log2n)
# SC - O(1)