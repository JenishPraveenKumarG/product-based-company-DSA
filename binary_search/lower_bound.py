def lower_bound(arr,target):
    low = 0
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            ans = mid
            high = mid -1 
        else:
            low = mid + 1
    return ans

arr = [1,2,3,4,5,6,7]
target = 6
print(lower_bound(arr,target))
            
