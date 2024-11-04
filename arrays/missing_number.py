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
    n = 5
    hash = [0]*(n+1)
    for i in a:
        hash[i] = 1
    for i in range(1,len(hash)):
        if hash[i]== 0:
            return i
    return 0

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

# optimised solution using xor


def missingNumber(a):
    n = len(a)
    xor1 = 0
    xor2 = 0

    '''for i in range(1,n+2):
      xor1 ^= i'''

    for i in range(n):
       xor2 ^= arr[i]
       xor1 ^= i+1
    
    xor1 = xor1 ^ (n+1)
    
    return xor1 ^ xor2
      

arr = [1,3,4,5]
print(missingNumber(arr))