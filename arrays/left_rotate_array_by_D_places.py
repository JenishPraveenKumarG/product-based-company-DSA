# brute

def left_rotate_D(arr,k):
    n = len(arr)
    k = k%n
    temp = arr[:k]
    for i in range(k,n):
        arr[i-k] = arr[i]
    '''
    j = 0
    for i in range(n-k,n):
        arr[n-k] = temp[j]
        j+=1'''
    
    print(temp)
    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]
    return arr

arr = [1,2,3,4,5,6]
k = 3
print(left_rotate_D(arr,k))


# TC - O(d) + O(n) + O(d)
# SC - O(d)


# Optimal solution

def reverse(arr,l,r):
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    
    return arr

def left_rotate_D(arr,k):
    n = len(arr)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

arr = [1,2,3,4,5,6]
k = 3
print(left_rotate_D(arr,k))

# TC - O(d) + O(n-d) + O(n) = O(2n)
# SC - O(1)

