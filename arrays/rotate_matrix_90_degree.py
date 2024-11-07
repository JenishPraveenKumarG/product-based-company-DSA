# Brute solution

def rotate_matrix_zeros(arr):
    n = len(arr)
    m = len(arr[0])
    ans = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ans[j][n-1-i] = arr[i][j]
    return ans

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,15]]
print(rotate_matrix_zeros(arr))

# TC - O(n x m) 
# SC - O(n x m)

# optimsed solution using inplace


def reverse(i):
    l = 0
    r = len(i)-1

    while l<=r:
        i[l],i[r] = i[r],i[l]
        l+=1
        r-=1
    return i

def rotate_matrix_zeros(arr):
    n = len(arr)
    m = len(arr[0])
    
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    for i in arr:
        i = reverse(i)
    
    return arr

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,15]]
print(rotate_matrix_zeros(arr))