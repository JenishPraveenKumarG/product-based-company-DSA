def converter(string):
    ans = 0
    s = string[::-1]
    for i in range(len(string)):
        ans+= int(s[i]) * 2**i
    
    return ans

string = '1101'
print(converter(string))

# TC - log2n
# SC - log2n


def converter(string):
    ans = 0
    s = string[::-1]
    p_of_2 = 1
    for i in range(len(s)):
        if s[i] == '1':
            ans += p_of_2
        p_of_2 *= 2

    return ans

string = '1101'
print(converter(string))

# TC - log2n
# SC - log2n