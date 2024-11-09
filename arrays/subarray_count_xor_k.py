def subarray(arr,val):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i,n):
            xorr = 0
            for k in range(i,j+1):
                xorr = xorr ^ arr[k]
            if xorr == val:
                count += 1
    return count
    

arr = [4,2,2,6,4]
k = 6
print(subarray(arr,k))

# TC - O(n**3)
# SC - O(1)


#Better solution

def subarray(arr,val):
    count = 0
    n = len(arr)

    for i in range(n):
        xor = 0
        for j in range(i,n):
            xor ^= arr[j]
            if xor == val:
                count += 1
    return count
    

arr = [4,2,2,6,4]
k = 6
print(subarray(arr,k))

# TC - O(n**2)
# SC - O(1)

# optimal solution

def subarray(arr,val):
    count = 0
    xor = 0
    mpp = {}
    mpp[count] = 1
    n = len(arr)
    for i in range(n):
        xor = xor^arr[i]
        x = xor ^ val
        if x in mpp:
            count+=mpp[x]
        
        if xor not in mpp:
            mpp[xor] = 0
        mpp[xor]+=1
    return count
    

arr = [4,2,2,6,4]
k = 6
print(subarray(arr,k))

# TC - O(n)
# SC - O(n)