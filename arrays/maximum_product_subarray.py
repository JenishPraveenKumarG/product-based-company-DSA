# brute solution

def max_prod(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            prod =1
            for k in range(i,j):
                prod *= arr[k]
            ans = max(prod,ans)
    return ans

arr = [2,3,-2,4]
print(max_prod(arr))

# TC - O(n**3)
# SC - O(1)

# better solution

def max_prod(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        prod = 1
        for j in range(i,n):
            prod *= arr[j]
            ans = max(prod,ans)
            
    return ans

arr = [2,3,-2,4]
print(max_prod(arr))

# TC - O(n**2)
# SC - O(1)

# optimal solution - 1 (observation based)

'''
1. if everythin is positive ans > 0 ---> multiply everything
2. if even number of negatives ---> multiply everything
3. if odd negatives ---> observae abd ignore 1 negative 
4. if zeros 
'''

# get all prefix and get all suffix

def max_prod(arr):
    maxi = 0
    prefix = 1
    suffix = 1
    n = len(arr)
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix * arr[i]
        suffix = suffix * arr[n-i-1]
        maxi = max(maxi,max(prefix,suffix))
    return maxi

arr = [2,3,-2,4]
print(max_prod(arr))

# TC - O(n)
# sC - O(1)
