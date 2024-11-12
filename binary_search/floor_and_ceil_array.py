# ceil - largest number in the array <= x
# floor - smallest number in the array >= x

def floor(arr,target):
    low = 0
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid -1
    return ans

arr = [10,20,30,40]
print(floor(arr,25))


def floor(arr,target):
    low = 0
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [10,20,30,40]
print(floor(arr,25))


