# array has unique elements

def how_many(arr):
    low = 0
    high = len(arr)-1
    ans = float('inf')
    while low<=high:
        mid = (low + high)//2
        if arr[low]<=arr[high]:
            ans = low
            break

        if arr[low] <= arr[mid]:
            ans = low
            low = mid + 1
        elif arr[low] > arr[mid]:
            ans = mid
            high = mid - 1
        else:
            continue

    return ans

arr = [3,4,5,1,2]
# ans is 3 ---> we have to find the minimum and return its index
print(how_many(arr))