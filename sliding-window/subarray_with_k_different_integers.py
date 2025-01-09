def print_count(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            seen.add(arr[j])
            if len(seen) == k:
                cnt+=1
            elif len(seen) > k:
                break
    
    return cnt

arr = [1,2,1,3,4]
k = 3
print(print_count(arr))

# TC - O(n x n)
# Sc - O(n) - worst case where everything is unique


# optimization

def print_count(arr,k):
    ''' find the number of subarrays <= k'''
    n = len(arr)
    l = 0
    cnt = 0
    mpp = {}

    for r in range(n):
        val = arr[r]
        if val not in mpp:
            mpp[val] = 0
        mpp[val]+=1

        while len(mpp) > k:
            left = arr[l]
            mpp[left] -= 1
            if mpp[left] == 0:
                del mpp[left]
            l+=1
        
        cnt += r-l+1
        
    return cnt


arr = [1,2,1,3,4]
k = 3
total = print_count(arr,k) - print_count(arr,k-1)
print(total)

# TC -2 x  O(2n)
# SC - 2 x O(n)

