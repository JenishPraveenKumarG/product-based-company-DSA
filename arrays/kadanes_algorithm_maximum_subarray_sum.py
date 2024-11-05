# Brute solution

def max_sub_sum(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j):
               sum+=arr[k]
            max_sum = max(sum,max_sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
print(max_sub_sum(arr))

# TC - O(n**3)
# SC - O(1)


# Better solution

def max_sub_sum(arr):
    max_sum = float('-inf')
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            max_sum = max(max_sum,sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
print(max_sub_sum(arr))

# TC - O(n**2)
# SC - O(1)

# Optimal solution - kadanes algorithm

def max_sub_sum(arr):
    max_sum = float('-inf')
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum < 0:
            sum= 0
        else:
            max_sum = max(max_sum,sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
print(max_sub_sum(arr))

# TC - O(n)
# SC - O(1)