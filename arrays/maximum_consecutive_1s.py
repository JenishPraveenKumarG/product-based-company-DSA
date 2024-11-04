def max_1s(arr):
    maxi = 0
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            count+=1
            maxi = max(maxi,count)
        else:
            count = 0
    return maxi

arr = [1,1,0,1,1,1,0,1,1]
print(max_1s(arr))

# TC - O(n)
# SC - O(1)