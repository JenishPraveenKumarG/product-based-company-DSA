def converter(n):
    res = ''
    while n>0:
        if n%2 == 1:
            res+='1'
        else:
            res+='0'
        n = n//2
    return res[::-1]

n = 13
print(converter(n))

# TC - log2n
# SC - log2n




