def check(val,n):
    ans = 1
    for i in range(n):
        ans = ans*val
    
    return ans

def nth(n,m):
    
    for i in range(1,m):
        if check(i,n) == m:
            return i
        if check(i,n) > m:
            return -1

print(nth(3,27))


# thats look clumsy so lets do binary serch

def nth(n,m):
    low = 1
    high = m

    while low <= high:
        mid = (low+high)//2
        if check(mid,n) == m:
            return mid
        elif check(mid,n) < m:
            low = mid + 1   
        else:
            high = mid - 1
    return -1

print(nth(3,27))