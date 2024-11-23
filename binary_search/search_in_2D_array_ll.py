def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == target:
                return [i,j]
    return [-1,-1]
    
arr = [[1,4,7,11],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 14
print(search_2D(arr,target))

# TC - O(n x m)
# SC - O(1)

# SInce each row is sorted we gonna apply binary search in each array in the matrix

def bs(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    
    for i in range(n):
        if arr[i][0] <= target and arr[i][-1] >= target:
            ans = bs(arr[i],target)
            if ans!= -1:
                return [i,ans]
    
    return [-1,-1]

arr = [[1,4,7,11],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 14
print(search_2D(arr,target))

# TC - O(n x log2n)
# SC - O(1)



# lets optimise this

def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])

    row = 0
    col = m-1

    while row < n and col >=0:
        if arr[row][col] == target:
            return [row,col]
        elif arr[row][col] < target:
            row += 1
        else:
            col -= 1
    return [-1,-1]
    

arr = [[1,4,7,11],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 14
print(search_2D(arr,target))

# TC - O(n+m) for taking the steps row ++ and col --
# SC - O(1)