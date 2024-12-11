def ans(divident,divisor):
    sum = 0
    cnt = 0

    while sum + divisor < divident:
        cnt+=1
        sum+=divisor
    
    return cnt

divident = 22
divisor = 3
print(ans(divident,divisor))

# TC - O(divident)
# SC - O(1)

def ans(divident,divisor):
    if divident == divisor:
        return 1
    
    sign = True

    if divident < 0 and divisor > 0:
        sign = False
    
    if divident > 0 and divisor < 0:
        sign = False

    n = abs(divident)
    d = abs(divisor)
    ans = 0

    while n>=d:
        cnt = 0

        while n >= (d<<(cnt+1)):
            cnt+=1
        
        ans += 1 << cnt #= 2**cnt

        n = n-(d * (1<<cnt))
    return ans

divident = 10
divisor = 3
print(ans(divident,divisor))

# TC - O(divident)
# SC - O(1)

