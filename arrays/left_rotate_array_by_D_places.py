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

