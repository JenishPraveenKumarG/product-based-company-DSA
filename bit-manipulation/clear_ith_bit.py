# brute will be converting the number to binary and then changing the ith bit


# using xor

n = 13
bit = 2

val = 1 << bit
print(n ^ val)

# using ans

n = 13
bit = 2

val = 1 << bit
print(n & ~(val))

