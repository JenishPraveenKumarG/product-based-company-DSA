def sub_set(arr, n):
    ans = []

    def helper(idx, sum):
        if idx == n:
            ans.append(sum)
            return
        helper(idx+1, sum + arr[idx])

        helper(idx + 1, sum)
    
    helper(0,0)
    ans.sort()
    return ans

arr = [3,1,2]
ans = sub_set(arr,len(arr))
print(ans)