def jump_game(arr):
    r = 0
    n = len(arr)
    jumps = 0
    l = 0
    far = 0
    while r < n-1:
        for i in range(l,r+1):
            far = max(far,i+arr[i])

        l = r+1
        r = far
        jumps += 1
    
    return jumps

arr = [2,3,0,1,4]
print(jump_game(arr))

# TC - O(n)
# SC - O(1)