# brute solution

def max_1s(arr):
    n = len(arr)
    m = len(arr[0])
    maxi = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1

        maxi = max(maxi,cnt)
    return maxi
            

arr = [[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
print(max_1s(arr))

# TC - O(n x m)

# optimise this
''' what we gona do is to find the frist occurance of 1 in eaxh array in matrix and then m - foccurance will be the 
    the number of 1s in that array'''

def lower_bound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans



def max_1s(arr):
    n = len(arr)
    m = len(arr[0])
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lower_bound(arr[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index
            

arr = [[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
print(max_1s(arr))

# TC - O(n x log2n)
# SC - O(1)