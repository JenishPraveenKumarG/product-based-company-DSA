def sqrt(n):
    return int(n**0.5)

print(sqrt(9))


# thats cheating man lets do it properly using binary search

def sqrt(n):
    low = 1
    high = n

    while low <=high:
        mid = (low + high)//2
        mid_sq = mid * mid

        if mid_sq == n:
            return mid
                
        elif mid_sq > n:
            high = mid - 1
        
        else:
            low = mid + 1
    
    return high

print(sqrt(10))

