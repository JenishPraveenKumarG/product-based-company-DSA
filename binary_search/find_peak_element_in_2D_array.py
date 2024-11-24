def max_element(arr,n,m,col):
    max_value = -1
    index = -1
    for i in range(n):
        if arr[i][col] > max_value:
            max_value = arr[i][col]
            index = i
    return index


def find_peak(arr):
    n = len(arr)
    m = len(arr[0])

    low = 0
    high = m-1

    while low <= high:
        mid = (low + high)//2
        row = max_element(arr,n,m,mid)

        if mid - 1>=0:
            left = arr[row][mid-1]
        else:
            left = -1
        if mid +1 < m:
            right = arr[row][mid+1]
        else:
            right = -1

        if arr[low][mid] > left and arr[row][mid] > right:
            return [row,mid]
    
        elif arr[row][mid] < left:
            high = mid - 1

        else:
            low = mid + 1

    return [-1,-1]


arr = [[4,2,5,1,4,2],[2,9,3,2,3,2],[1,7,6,0,2,1,3],[3,6,2,3,7,2]]
print(find_peak(arr))