def longest(s,k):
    n = len(s)
    maxLen = 0
    maxFreq = 0
    for i in range(n):
        hash = [0]*26
        for j in range(i,n):
            hash[ord(s[j])-ord('A')] += 1
            maxFreq = max(maxFreq,hash[ord(s[j])-ord('A')])
            changes = (j-i+1) - maxFreq
            if changes <= k:
                maxLen = max(maxLen,j-i+1)
            else:
                break
    return maxLen

s = "AABABBA"
k = 2
print(longest(s,k))

# TC - o(n x n)
# Sc - O(26)

# using 2 pointer-sliding window

def longest(s,k):
    n = len(s)
    l = 0
    r = 0
    maxLen = 0
    maxFreq = 0
    hash = [0]*26

    while r < n:
        hash[ord(s[r]) - ord('A')] += 1
        maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
        while (r-l+1) - maxFreq > k:
            hash[ord(s[l]) - ord('A')]-=1
            maxFreq = 0
            for i in range(26):
                maxFreq = max(maxFreq,hash[i])
            l+=1

        if (r - l + 1) - maxFreq <= k:
            maxLen = max(maxLen,r-l+1)
        r+=1
    return maxLen

s = "AABABBA"
k = 2
print(longest(s,k))

# TC - O(n + n) * 26
# Sc - O(26)

# optimised solution

def longest(s,k):
    n = len(s)
    l = 0
    r = 0
    maxLen = 0
    maxFreq = 0
    hash = [0]*26

    while r < n:
        hash[ord(s[r]) - ord('A')] += 1
        maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
        if (r-l+1) - maxFreq > k:
            hash[ord(s[l]) - ord('A')]-=1
            maxFreq = 0
            l+=1

        if (r - l + 1) - maxFreq <= k:
            maxLen = max(maxLen,r-l+1)
        r+=1
    return maxLen

s = "AABABBA"
k = 2
print(longest(s,k))

# TC - O(n)
# Sc - O(26)