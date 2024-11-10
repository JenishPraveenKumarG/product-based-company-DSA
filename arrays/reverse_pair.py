def reverse_pair(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(i+1,n):
            if arr[i] > (2 * arr[j]):
                cnt+=1
        count+=cnt
    
    return count

arr = [40, 25, 19,12,9, 6, 2]
print(reverse_pair(arr))

# TC - O(n**2)
# SC - O(1)

# optimal solution

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    cnt = 0
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += mid - left + 1
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

def count_pairs(arr,low,mid,high):
    cnt = 0
    right = mid+1
    for i in range(low,mid+1):
        while right <= high and arr[i] > 2*arr[right]:
            right += 1
        cnt += right - (mid+1)

    return cnt



def mergeSort(arr,low,high):
    cnt = 0
    if low>=high:
        return cnt
    mid = (low+high)//2
    cnt += mergeSort(arr,low,mid)
    cnt += mergeSort(arr,mid+1,high)
    cnt += count_pairs(arr,low,mid,high)
    merge(arr,low,mid,high)
    return cnt

def reverse_pair(arr):
    n = len(arr)
    return mergeSort(arr,0,n-1)

arr = [40, 25, 19,12,9, 6, 2]
print(reverse_pair(arr))

# TC - O(logn) for dividing array + O(n1 + n2) for count_pair function
# SC - O(n) for merge sort
