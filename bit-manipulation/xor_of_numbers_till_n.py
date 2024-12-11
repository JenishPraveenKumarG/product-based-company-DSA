def xor(n):
    xorr = 0
    for i in range(1,n+1):
        xorr ^= i

    return xorr

n = 4
print(xor(n))

# TC - O(n)
# SC - O(1)

def xorr(n):
    if n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    elif n%4 == 3:
        return 0
    else:
        return n

n = 4
print(xorr(n))

# TC - O(1)
# SC - O(1)


''' To find the xor between range '''

l = 4
r = 7
# between this range we need to find the answer

print(xorr(l-1) ^ xorr(r))