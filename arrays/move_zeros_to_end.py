# Brute solution

def move_zeros(arr):
    temp = []
    n1 = len(arr)
    
    for i in arr:
        if i != 0:
            temp.append(i)

    n2 = len(temp)
    for i in range(n2):
        arr[i] = temp[i]

    for i in range(n2,n1):
        arr[i] = 0
    
    return arr

arr = [1,0,2,0,3,0,4,0]
print(move_zeros(arr))

# TC - O(n) + O(x) + O(n-x) = O(2n)
# SC - O(n)


# optimal solution

def move_zeros(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(0)
    return arr


arr = [1,0,2,0,3,0,4,0]
print(move_zeros(arr))

# TC - O(n)
# SC - O(1)

# second optimal solution

def move_zeros(arr):
    n = len(arr)
    r = 0  
    
    for l in range(n):
        if arr[l] != 0:  
            arr[l], arr[r] = arr[r], arr[l]
            r += 1 

    return arr

arr = [1,0,2,0,3,0,4,0]
print(move_zeros(arr))

# TC - O(n)
# SC - O(1)