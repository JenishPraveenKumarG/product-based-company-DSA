# brute solution

def sub_array_ranges(arr):
    cnt = 0
    n = len(arr)
    for i in range(n):
        maxi = arr[i]
        mini = arr[i]
        for j in range(i+1,n):
            maxi = max(arr[j],maxi)
            mini = min(mini,arr[j])
            cnt += maxi - mini
    
    return cnt 

arr = [1,4,3,2]
print(sub_array_ranges(arr))

# TC - O(n**2)
# SC - O(1)


# optimal solution

def find_nse(arr):
    stack = []
    n = len(arr)
    nse = [0]*n
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            nse[i] = n
        else:
            nse[i] = stack[-1]
        stack.append(i)
    return nse

def find_pse(arr):
    stack = []
    n = len(arr)
    pse = [0]*n
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] > arr[i]:
            stack.pop()
        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]
        stack.append(i)
    return pse

def find_nge(arr):
    stack = []
    n = len(arr)
    nge = [0]*n
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            nge[i] = n
        else:
            nge[i] = stack[-1]
        stack.append(i)
    return nge

def find_pge(arr):
    stack = []
    n = len(arr)
    pge = [0]*n
    for i in range(n):
        while len(stack) != 0 and arr[stack[-1]] < arr[i]:
            stack.pop()
        if len(stack) == 0:
            pge[i] = -1
        else:
            pge[i] = stack[-1]
        stack.append(i)
    return pge

def subarray_range_sum(arr):
    n = len(arr)
    pse = find_pse(arr)
    nse = find_nse(arr)
    pge = find_pge(arr)
    nge = find_nge(arr)
    
    total = 0
    for i in range(n):
        # Contribution as minimum
        left_min = i - pse[i]
        right_min = nse[i] - i
        min_contribution = left_min * right_min * arr[i]
        
        # Contribution as maximum
        left_max = i - pge[i]
        right_max = nge[i] - i
        max_contribution = left_max * right_max * arr[i]
        
        # Add both contributions
        total += max_contribution - min_contribution

    return total

# Test case
arr = [1,4,3,2]
print(subarray_range_sum(arr))  

# TC - O(2n + 2n + 2n + 2n + n) approx - 10n
# SC - O(2n + 2n + 2n + 2n + n) approx - 10n
