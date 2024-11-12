def search_position(arr,target):
    low = 0
    ans = -1
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1
    return ans

arr=[1,2,4,7]
t1 = 6
t2 = 2
print(search_position(arr,t1))
print(search_position(arr,t2))