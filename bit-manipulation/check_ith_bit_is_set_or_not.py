# Brute solution

def converter(n):
    res = ''
    while n>0:
        if n%2 == 1:
            res+='1'
        else:
            res+='0'
        n = n//2
    return res

n = 13
bit = 2
a = converter(n)

if len(a)<bit:
    print(False)

if a[bit] == '1':
    print(True)
else:
    print(False)


# using bit wise operators left shift

n = 13
bit = 2

val = 1 << bit

ans = n & val
if ans:
    print(True)
else:
    print(False)


# using right shift

n = 13
bit = 2

n = n >> bit

ans = n&1

if ans:
    print(True)
else:
    print(False)

