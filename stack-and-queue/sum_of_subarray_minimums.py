# brute solution

def sub_array_minimum(arr):
    sum = 0
    n = len(arr)
    for i in range(n):
        mini = arr[i]
        for j in range(i,n):
            mini = min(mini,arr[j])
            sum += mini
    return sum 

arr = [3,1,2,4]
print(sub_array_minimum(arr))

# TC - O(n**2)
# SC - O(1)

# optimised solution


''' we will find the next smaller and previous smaller and find the contribution of each and every element how many times'''

def find_nse(arr):
    stack = []
    n = len(arr)
    nse = [0]*n
    for i in range(n-1,-1,-1):
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


def sub_array_mini(arr):
    nse = find_nse(arr)
    pse = find_pse(arr)
    print(pse)
    print(nse)
    total = 0
    for i in range(len(arr)):
        left = i - pse[i]
        right = nse[i] - i

        total += right * left * arr[i]
    
    return total

arr = [3,1,2,4]
print(sub_array_mini(arr))

# TC - O(5n)
# SC - O(5n)