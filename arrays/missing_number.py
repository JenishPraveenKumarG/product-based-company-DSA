# Brute force solution

def missingNumber(arr):
    n = len(arr)
    for i in range(1,n+1):
        if i not in arr:
            return i
    return 0

arr = [1,3,4,5]
print(missingNumber(arr))

# TC - O(n * w)
# SC - O(1)



# Better solution using hash array


def missingNumber(a):
    N = len(a)+1
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

arr = [1,3,4,5]
print(missingNumber(arr))



# optimised solution using mathematics

def missingNumber(arr):
    n = len(arr)

    sum = 0
    for num in arr:
        sum+=num
        
    n = (n*(n+1))//2
    return n-sum

arr = [1,3,4,5]
print(missingNumber(arr))

# TC - O(n)
# SC - O(1)