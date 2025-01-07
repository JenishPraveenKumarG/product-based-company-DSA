def basket(arr):
    n = len(arr)
    maxlen = 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            seen.add(arr[j])
            if len(seen) <= 2:
                maxlen = max(maxlen,j-i+1)
            else:
                break
    return maxlen

arr = [3,3,3,1,2,1,1,2,3,3,4]
print(basket(arr))

# TC - O(n x n)
# SC - O(3)

# better solution

def basket(arr):
    n =  len(arr)
    mpp = {}
    maxlen = 0
    l = 0
    r = 0
    while r < n:
        if arr[r] not in mpp:
            mpp[arr[r]] = 0
        mpp[arr[r]]+= 1

        while len(mpp) > 2:
            left = arr[l]
            mpp[left]-=1
            if mpp[left] == 0:
                del mpp[left]
            l+=1
        maxlen = max(maxlen,r-l+1)
        r+=1


    return maxlen


arr = [3,3,3,1,2,1,1,2,3,3,4]
print(basket(arr))

# TC -  O(2n)
# SC - O(3)

# most optimal solution

def basket(arr):
    n =  len(arr)
    mpp = {}
    maxlen = 0
    l = 0
    r = 0
    while r < n:
        if arr[r] not in mpp:
            mpp[arr[r]] = 0
        mpp[arr[r]]+= 1

        if len(mpp) > 2:
            left = arr[l]
            mpp[left]-=1
            if mpp[left] == 0:
                del mpp[left]
            l+=1
        if len(mpp) <=2:

            maxlen = max(maxlen,r-l+1)
        r+=1


    return maxlen


arr = [3,3,3,1,2,1,1,2,3,3,4]
print(basket(arr))

# TC - O(n)
# SC - O(3)
