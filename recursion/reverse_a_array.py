def reverse(arr,l,r):
    if l >= r:
        return arr
    arr[l],arr[r] = arr[r],arr[l]    
    return reverse(arr,l+1,r-1)

arr = [1,2,3,4]
low = 0
high = len(arr)-1
print(reverse(arr,low,high))


# using single variable

def reverse(arr,n,i):
    if i >=n:
        return arr
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    return reverse(arr,n,i+1)


arr = [1,2,3,4]
n = len(arr)//2
print(reverse(arr,n,0))