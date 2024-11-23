# Brute solution 

def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == target:
                return True
    
    return False


arr = [[3,4,7,9],[12,13,14,18],[20,21,23,24]]
target = 23
print(search_2D(arr,target))

# TC - O(n x m)
# SC - O(1)

# since every row is sorted we can check with start and end value of each array if the target is between that range means we can do a binary search


# optimal solution

def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        if arr[i][0] <= target and arr[i][-1] >= target:
            return binary_search(arr[i],target)
    
    return False


arr = [[3,4,7,9],[12,13,14,18],[20,21,23,24]]
target = 23
print(search_2D(arr,target))

# TC - O(n) + O(log2n)

# the above solution takes about O(n) approximately

''' we know the matrix is sorted , if we perfom bs on 1d array means TC - O(log2n)

    just in imaginary world we get this lets see how we are achieving this in our problem
    
    formula  mid//4 and then mid%4 '''

def search_2D(arr,target):
    n = len(arr)
    m = len(arr[0])
    low = 0
    high = (n*m-1)

    while low <= high:
        mid = (low + high)//2
        row = mid//m
        col = mid % 4

        if arr[row][col] == target:
            return True
        elif arr[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


arr = [[3,4,7,9],[12,13,14,18],[20,21,23,24]]
target = 23
print(search_2D(arr,target))

