def l_hist(arr):
    stack = []
    max_area = 0
    n = len(arr)

    for i in range(n + 1):  # Include an extra iteration for the "end of array" logic
        while len(stack) != 0 and (i == n or arr[stack[-1]] >= arr[i]):
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        if i < n:  # Avoid appending index `n`
            stack.append(i)
    return max_area


def maximal_rectangle(arr):
    n = len(arr)
    m = len(arr[0])
    pre_sum = [[0 for _ in range(m)] for _ in range(n)]
    
    # Compute prefix sum for columns
    for j in range(m):
        cur_sum = 0
        for i in range(n):
            if arr[i][j] == 1:
                cur_sum += 1
            else:
                cur_sum = 0
            pre_sum[i][j] = cur_sum

    # Find the maximal rectangle using largest histogram approach
    new_area = 0
    for i in range(n):
        new_area = max(new_area, l_hist(pre_sum[i]))

    return new_area


# Input array
arr = [[1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
print(maximal_rectangle(arr))

# TC - O(m x n) + O(2m)
# SC - O(n x m) + O(n)