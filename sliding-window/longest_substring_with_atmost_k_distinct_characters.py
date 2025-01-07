def longest(string,k):
    n = len(string)
    maxlen = 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            seen.add(string[j])
            if len(seen) <= k:
                maxlen = max(maxlen,j-i+1)
            else:
                break
    return maxlen

string = "aaabbccd"
k = 2
print(longest(string,k))

# TC - O(n x n)
# SC - O(k)

# better solution

def longest(string,k):
    n = len(string)
    maxlen = 0
    l = 0
    mpp = {}

    for r in range(n):
        val = string[r]
        if val not in mpp:
            mpp[val] = 0
        mpp[val]+=1

        while len(mpp) > k:
            left = string[l]
            mpp[left]-=1
            if mpp[left] == 0:
                del mpp[left]
            l+=1
        
        maxlen = max(maxlen,r-l+1)

    return maxlen

string = "aaabbccd"
k = 2
print(longest(string,k))

# TC - O(n + n)
# SC - O(3)

# optimal solution

def longest(string,k):
    n = len(string)
    maxlen = 0
    l = 0
    mpp = {}

    for r in range(n):
        val = string[r]
        if val not in mpp:
            mpp[val] = 0
        mpp[val]+=1

        if len(mpp) > k:
            left = string[l]
            mpp[left]-=1
            if mpp[left] == 0:
                del mpp[left]
            l+=1
        if len(mpp)<=k:
            maxlen = max(maxlen,r-l+1)

    return maxlen

string = "aaabbccd"
k = 2
print(longest(string,k))

# TC - O(n)
# SC - O(3)