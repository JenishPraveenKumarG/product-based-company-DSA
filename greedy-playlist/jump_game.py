def jump_game(arr):
    maxIndex = 0
    n = len(arr)
    for i in range(n):
        if i > maxIndex:
            return False
        maxIndex = max(maxIndex,i+arr[i])

    return True

arr1 = [2,3,1,0,4]
arr2 = [3,2,1,0,4]
print(jump_game(arr1))
print(jump_game(arr2))

# TC - O(n)
# SC - O(1)