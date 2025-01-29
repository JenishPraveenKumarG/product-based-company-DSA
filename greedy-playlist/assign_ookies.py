def assign_cookies(greed,s):
    greed.sort()
    s.sort()
    l = 0
    r = 0
    n = len(greed)
    m = len(s)
    cnt = 0
    while l<n and r<m:
        if greed[l] <= s[r]:
            cnt+=1
            l+=1
            r+=1
        elif greed[l] > s[r]:
            r+=1
        
        else:
            l+=1

    return cnt

    

greed = [1,5,3,3,4]
s = [4,3,1,2,1,3]
print(assign_cookies(greed,s))


# other solution 


def assign_cookies(greed,s):
    greed.sort()
    s.sort()
    l = 0
    r = 0
    n = len(greed)
    m = len(s)
    
    while l < n and r < m:
        if greed[l] <= s[r]:
            l+=1
        r+=1
    
    return l

    

greed = [1,5,3,3,4]
s = [4,3,1,2,1,3]
print(assign_cookies(greed,s))

# TC - O(nlogn) + O(mlogm) + O(m)