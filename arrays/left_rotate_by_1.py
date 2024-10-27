def left_rotate_1(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    
    arr[n-1] = temp
    return arr

arr = [1,2,3,4,5,6]
print(left_rotate_1(arr))

# TC - O(n)
# SC - O(1)
