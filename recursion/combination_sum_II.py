def combination_sum(idx,arr,target,ans,ds):
    if idx == len(arr):
        if target == 0:
            ans.add(tuple(ds[:]))
        return 

    if arr[idx] <= target:
        ds.append(arr[idx])
        combination_sum(idx+1,arr,target - arr[idx],ans,ds)
        ds.pop()
    
    combination_sum(idx+1,arr,target,ans,ds)



arr = [10,1,2,7,6,1,5]
target = 8
ans = set()
ds = []
combination_sum(0,arr,target,ans,ds)

def combination_sum(idx,arr,target,ans,ds):
    if idx == len(arr):
        if target == 0:
            ans.add(tuple(ds[:]))
        return 

    if arr[idx] <= target:
        ds.append(arr[idx])
        combination_sum(idx+1,arr,target - arr[idx],ans,ds)
        ds.pop()
    
    combination_sum(idx+1,arr,target,ans,ds)



arr = [10,1,2,7,6,1,5]
target = 8
ans = set()
ds = []
combination_sum(0,arr,target,ans,ds)

ans = [list(t) for t in ans]
print(ans)
# TC - 2**n x k + O(n)
#SC - O(ans) + O(n)


# optimal solution

def combination(arr,target):
    arr.sort()
    ds = []
    ans = []

    def find_combination(idx, target):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(idx, len(arr)):
            if i > idx and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break

            ds.append(arr[i])
            find_combination(i+1,target - arr[i])
            ds.pop()
    
    find_combination(0,target)
    return ans

arr = [10,1,2,7,6,1,5]
target = 8
ans = combination(arr,target)
print(ans)
