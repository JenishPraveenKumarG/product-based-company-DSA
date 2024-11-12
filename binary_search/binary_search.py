def bin_search(arr,low,high,target):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return bin_search(arr,mid+1,high,target)

    else:
        return bin_search(arr,low,mid-1,target)


arr = [3,4,6,7,9,12,16,17]
target = 12
print(bin_search(arr,0,len(arr)-1,target))