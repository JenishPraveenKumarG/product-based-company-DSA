def minimum_window(string,t):
    n = len(string)
    m = len(t)
    sIndex = -1
    minLen = float('inf')

    for i in range(n):
        mpp = {}
        cnt = 0

        for j in range(m):
            val = t[j]
            if val not in mpp:
                mpp[val] = 0
            mpp[val]+=1
    

        for j in range(i,n):
            val = string[j]
            if val in mpp:
                if mpp[val] > 0:
                    cnt+=1
                mpp[val]-=1

            if cnt == m:
                if j-i+1 < minLen:
                    minLen = j-i+1
                    sIndex = i
                break

    return string[sIndex:sIndex + minLen]


string = "ddaaabbca"
t = "abc"
print(minimum_window(string,t))

# TC - O(n x n)
# SC - O(t)


# optimal solution

def minimum_window(string, t):
    n = len(string)
    m = len(t)
    sIndex = -1
    minLen = float('inf')
    l = 0
    mpp = {}
    cnt = 0

    for char in t:
        if char not in mpp:
            mpp[char] = 0
        mpp[char] += 1

    for r in range(n):
        val = string[r]
        if val in mpp:
            if mpp[val] > 0:
                cnt += 1
            mpp[val] -= 1

        while cnt == m:
            if r - l + 1 < minLen:
                minLen = r - l + 1
                sIndex = l

            # Prepare to shrink the window
            left_char = string[l]
            if left_char in mpp:
                mpp[left_char] += 1
                if mpp[left_char] > 0:
                    cnt -= 1
            l += 1

    
    if sIndex == -1:
        return ""
    return string[sIndex:sIndex + minLen]


# Example usage
string = "ddaaabbca"
t = "abc"
print(minimum_window(string, t)) 

# TC - O(2n)
# Sc - O(t)