# Brute solution

def ele1(arr):
    n = len(arr)
    for i in range(n):
        element = arr[i]
        count = 0
        for j in range(n):
            if arr[j] == element:
                count+=1
        if count !=2:
            return element
    return 0

arr = [1,1,2,3,3,4,4]
print(ele1(arr))

# TC - O(n * n)
# SC - O(1)


# better solution using hashing

def ele1(arr):
    maxi = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]

    hash = [0]*(maxi + 1)

    for i in range(n):
        hash[arr[i]] +=1
    
    print(hash)
    for i in range(1,n):
        if hash[arr[i]] == 1:
            return arr[i]
    return 0

arr = [1,1,2,3,3,8,8]
print(ele1(arr))

# TC - O(n) + O(n) O(n)
# SC - O(max(arr))


# optimal solution using xor

def ele1(arr):
    xor1 = 0
    for i in arr:
        xor1= xor1 ^ i
    return xor1

arr = [1,1,2,3,3,8,8]
print(ele1(arr))

# TC - O(n)
# SC - O(1)