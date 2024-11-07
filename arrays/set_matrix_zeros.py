# Brute solution

def mark_row(i,arr):
    m = len(arr[0])
    for j in range(m):
        if arr[i][j]!= 0:
            arr[i][j] = -1
    return arr

def mark_col(j,arr):
    n = len(arr)
    for i in range(n):
        if arr[i][j]!= 0:
            arr[i][j] = -1
    return arr

def set_matrix_zeros(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                mark_row(i,arr)
                mark_col(j,arr)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0

    return arr

arr = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(set_matrix_zeros(arr))

# TC - O(n x m) + O(n+m) + O(n x m)
# SC - O(1)


# Better solution - instead of iterating the entire array if there exist one zero means we can say the entire row and col will be zero and this is the hint here

def set_matrix_zeros(arr):
    n = len(arr)
    m = len(arr[0])
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                row[i] = 1
                col[i] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                arr[i][j] = 0
    return arr

arr = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
print(set_matrix_zeros(arr))

# TC - o(n x m)
# SC - O(n) + O(m)


# optimal solution - tracking in place

def set_matrix_zeros(arr):
    n = len(arr)
    m = len(arr[0])
    col0 = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                # mark the ith row
                arr[i][0] = 0
                # mark the jth column
                if j != 0:
                    arr[0][j] = 0
                else:
                    col0 = 0
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j]!=0:
                if arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0
    if arr[0][0] == 0:
        for j in range(m):
            arr[0][j] == 0
    if col0 == 0:
        for i in range(n):
            arr[i][0] = 0
    return arr

arr = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
print(set_matrix_zeros(arr))

# TC - O(n x m)
# SC - O(1)



