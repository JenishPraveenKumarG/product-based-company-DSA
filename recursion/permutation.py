# solution 1
def perm(arr,ds,ans,freq):
    if len(ds) == len(arr):
        ans.append(ds[:])
        return
    
    for i in range(len(arr)):
        if freq[i] == False:
            freq[i] = True
            ds.append(arr[i])
            perm(arr,ds,ans,freq)
            ds.pop()
            freq[i] = False
    
    return ans

arr = [1,2,3]
ans = []
ds = []
freq = [False]*len(arr)
ans = perm(arr,ds,ans,freq)
print(ans)


# solution 2

def permutation(arr, n):
    ans = []
    
    def helper(idx, arr):
        if idx == n:
            ans.append(arr[:])  # Append a copy of the current permutation
            return

        for i in range(idx, n):
            
            if i > idx and arr[i] == arr[idx]:
                continue

            # Swap the current element with the element at idx
            arr[i], arr[idx] = arr[idx], arr[i]
            # Recur with the next index
            helper(idx + 1, arr)
            # Backtrack by swapping back
            arr[i], arr[idx] = arr[idx], arr[i]
    
    helper(0, arr)
    return ans

arr = [1, 2, 3]
ans = permutation(arr, len(arr))
print(ans)

# TC - n! x n

