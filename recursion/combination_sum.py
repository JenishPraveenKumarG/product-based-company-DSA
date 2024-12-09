def combination_sum(idx,arr,target,ans,ds):
    if idx == len(arr):
        if target == 0:
            ans.append(ds[:])
        return 
    
    if arr[idx] <= target:
        ds.append(arr[idx])
        combination_sum(idx,arr,target - arr[idx],ans,ds)
        ds.pop()
    
    combination_sum(idx+1,arr,target,ans,ds)



arr = [2,3,6,7]
target = 7
ans = []
ds = []
combination_sum(0,arr,target,ans,ds)

print(ans)