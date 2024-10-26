# brute solution

def rem_dup(arr):
    s = list(set(arr))
    idx = 0
    for i in s:
        arr[idx] = i
        idx+=1

    return idx

arr = [1,1,2,2,2,3,3]
print(rem_dup(arr))


# TC - O(nlogn) + O(n)
# SC - O(n)
 

# Optimal approach

def rem_dup(arr):
    l = 0
    r = l+1
    n = len(arr)

    while r<n:
        if arr[l]!=arr[r]:
            l+=1
            arr[l] = arr[r]
            r+=1
        else:
            r+=1

    return l

arr = [1,1,2,2,2,3,3]
print(rem_dup(arr))