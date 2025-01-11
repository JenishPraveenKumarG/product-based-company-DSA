def number_of_substr(string):
    n = len(string)
    cnt = 0

    for i in range(n):
        mpp = {}
        for j in range(i,n):
            cur_val = string[j]
            if cur_val not in mpp:
                mpp[cur_val] = 0
            mpp[cur_val] += 1

            if 'a' in mpp and 'b' in mpp and 'c' in mpp:
                cnt += 1
    
    return cnt

string = "abcabc"
print(number_of_substr(string))

# TC - O(n x n)
# Sc - O(3)


# optimization

def number_of_substr(string):
    n = len(string)
    cnt = 0

    for i in range(n):
        mpp = {}
        for j in range(i,n):
            cur_val = string[j]
            if cur_val not in mpp:
                mpp[cur_val] = 0
            mpp[cur_val] += 1

            if 'a' in mpp and 'b' in mpp and 'c' in mpp:
                cnt += n-j
                break
    
    return cnt

string = "abcabc"
print(number_of_substr(string))

# optimal solution

def number_of_substr(string):
    n = len(string)
    cnt = 0
    mpp = {'a' : -1, 'b':-1, 'c':-1}

    for i in range(n):
        mpp[string[i]]=i
        if mpp['a']!=-1 and mpp['b']!=-1 and mpp['c']!=-1:
            cnt+=min(mpp['a'],mpp['b'],mpp['c'])+1
    return cnt

string = "abcabc"
print(number_of_substr(string))

# TC - O(n)
# SC - O(3)