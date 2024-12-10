def subset(arr, n):
    ans = []
    res = set()

    def helper(idx, ds):
        if idx == n:
            ds.sort()
            res.add(tuple(ds))
            return
        ds.append(arr[idx])
        helper(idx+1, ds)
        ds.pop()
        helper(idx+1, ds)

    helper(0,[])

    for i in res:
        ans.append(i)
    return ans

arr = [1,2,3]
ans = subset(arr,len(arr))
ans = [list(t) for t in ans]
print(sorted(ans))

