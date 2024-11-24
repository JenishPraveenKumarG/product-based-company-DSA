def upper_bound(arr,target,n):
    ans = n
    high = n-1
    low = 0

    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def count_small(arr,n,m,x):
    cnt = 0
    for i in range(n):
        cnt += upper_bound(arr[i],x,m)
    return cnt


def median(arr):
    '''brute solution we will add all values in a new 1D array
        
        and then sort the array and return the median (middle elemen)
        
        # TC - O(n x m) + O(m x n xlog2n)'''
    
    n = len(arr)
    m = len(arr[0])

    low = float('inf')
    high = float('-inf')

    for i in range(n):
        low = min(low, arr[i][0])
        high = max(high,arr[i][m-1])

    req = (m * n)//2

    while low <= high:
        mid = (low + high)//2
        small_equal = count_small(arr,n,m,mid)
        if small_equal <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low

    


arr = [[1,5,7,9,11],[2,3,4,5,10],[9,10,12,14,16]]
print(median(arr))

# TC - O(log2 10**9) x O(n) x O(log2m)