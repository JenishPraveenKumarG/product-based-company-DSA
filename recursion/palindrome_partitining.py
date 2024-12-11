def is_palindrome(s,start,end):
    while start <= end:
        if s[start]!= s[end]:
            return False
        start +=1
        end -= 1
    return True

def partition(s):
    res = []
    path = []

    def helper(idx):
        if idx ==len(s):
            res.append(path[:])
            return
        
        for i in range(idx,len(s)):
            if is_palindrome(s,idx,i):
                path.append(s[idx:i+1])
                helper(i+1)
                path.pop()

    helper(0)
    return res



s = 'aabb '
ans = partition(s)
print(ans)