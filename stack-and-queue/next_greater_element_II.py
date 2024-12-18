def next_greater(arr):
    n = len(arr)
    ans = [-1]*n
    for i in range(n):
        for j in range(i+1,i+n):
            idx = j%n
            if arr[idx] > arr[i]:
                ans[i] = arr[idx]
                break
    return ans

arr = [2,10,12,1,11]
print(next_greater(arr))

# TC - O(n**2)
# SC - O(n)

# optimal solution

def next_greater(arr):
    n = len(arr)
    stack = []
    ans = [-1] * n  # Initialize with -1 for all elements

    for i in range(2 * n - 1, -1, -1):
        while stack and stack[-1] <= arr[i % n]:
            stack.pop()

        if i < n:
            if stack:
                ans[i] = stack[-1]

        stack.append(arr[i % n])

    return ans

arr = [2,10,12,1,11]
print(next_greater(arr))