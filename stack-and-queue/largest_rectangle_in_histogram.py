# brute solution - we will find the min and max and then multiply them

def largest_area_rectangle(arr):
    max_area = 0
    n = len(arr)
    for i in range(n):
        mini = float('inf')
        for j in range(i,n):
            mini = min(mini,arr[j])
            max_area = max(max_area,mini*(j-i+1))
    return max_area

arr = [2,1,5,6,2,3]
print(largest_area_rectangle(arr))

# TC - O(n x n)
# SC - O(1)


# better solution -- we need pse and nse

def pse(arr):
    stack = []
    ans = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(i)
    return ans

def nse(arr):
    stack = []
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        ans[i] = stack[-1] if stack else len(arr)
        stack.append(i)
    return ans

def largest_area_rectangle(arr):
    right = nse(arr)
    left = pse(arr)
    max_area = 0
    for i in range(len(arr)):
        max_area = max(max_area, arr[i] * (right[i] - left[i] - 1))
    return max_area

arr = [2, 1, 5, 6, 2, 3]
print(largest_area_rectangle(arr))

# TC - O(2n) + O(2n) +O(n)
# SC - O(5n)


# optimal solution


def largest_area_rectangle(histo):
    stack = []
    max_area = 0
    n = len(histo)

    for i in range(n + 1):
        while stack and (i == n or histo[stack[-1]] >= histo[i]):
            height = histo[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * height)
        stack.append(i)

    return max_area

histo = [2, 1, 5, 6, 2, 3]
print(largest_area_rectangle(histo))

# TC - O(n) + O(n)
# SC - O(n)
