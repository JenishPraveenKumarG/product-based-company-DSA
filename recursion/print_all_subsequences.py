def sub(idx,arr,ds,n):
    if idx >= n:
        print(ds)
        return
    
    ds.append(arr[idx])
    sub(idx + 1, arr,ds,n)
    ds.pop()
    sub(idx + 1, arr,ds,n)


arr = [3,1,2]
ds = []
n = len(arr)
sub(0,arr,ds,n)

# TC - O(2 power n) x n
# SC - O(n)