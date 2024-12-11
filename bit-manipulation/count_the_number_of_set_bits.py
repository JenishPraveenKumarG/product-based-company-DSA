def count_set_bits(n):
    cnt = 0

    while n > 1:
        if n%2 == 1:
            cnt += 1
        n = n//2
    
    if n == 1:
        cnt +=1
    
    return cnt

print(count_set_bits(13))


# using operator


def count_set_bits(n):
    cnt = 0

    while n > 1:
        if n&1:
            cnt += 1
        
        n = n >> 1
    
    if n == 1:
        cnt +=1
    
    return cnt

print(count_set_bits(13))



# another methods


def count_set_bits(n):
    cnt = 0

    while n != 0:
        cnt +=1
        n = n & n-1
    
    return cnt

print(count_set_bits(13))

# TC - Log2(start ^ goal)
# SC - O(1)