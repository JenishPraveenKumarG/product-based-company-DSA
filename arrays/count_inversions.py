def count_inversion(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                cnt+=1
        count+=cnt
    
    return count

arr = [5,3,2,4,1]
print(count_inversion(arr))

# TC - O(n**2)
# SC - O(1)


# optimal approach

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    cnt = 0  # this counts
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += mid - left + 1  # here it is the big guy
            right += 1
        
    while left <= mid:
        temp.append(arr[left])
        left+=1
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low,high+1):
        arr[i] = temp[i-low]
    
    return cnt

def mergeSort(arr,low,high):
    cnt = 0
    if low>=high:
        return cnt
    mid = (low+high)//2
    cnt += mergeSort(arr,low,mid)
    cnt += mergeSort(arr,mid+1,high)
    cnt += merge(arr,low,mid,high)
    return cnt

def count_inversion(arr):
    n = len(arr)
    return mergeSort(arr,0,n-1)

arr = [5,3,2,4,1]
print(count_inversion(arr))
