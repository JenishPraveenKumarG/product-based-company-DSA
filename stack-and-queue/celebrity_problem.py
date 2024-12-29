def celebrity(arr):
    n = len(arr)
    known = [0]*n
    i_known = [0]*n

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                known[j]+=1
                i_known[i]+=1
    
    for i in range(n):
        if known[i] == n-1 and i_known[i] == 0:
            return i

arr = [[0,1,1,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
print(celebrity(arr))

# TC - O(n x n)
# SC - O(2n)

# optimal solution

def celebrity(arr):
    n = len(arr)
    top = 0
    down = n-1

    while top < down:
        if arr[top][down] == 1:
            top +=1
        elif arr[down][top] == 1:
            down -= 1
        else:
            top += 1
            down -= 1
    
    if top > down:
        return -1

    for i in range(n):
        if i == top:
            continue
        if arr[top][i] == 0 and arr[i][top] == 1:
            continue
        else:
            return -1
    
    return top


arr = [[0,1,1,0],[0,0,0,0],[0,1,0,0],[1,1,0,0]]
print(celebrity(arr))

# TC - O(2n)
# SC - O(1)