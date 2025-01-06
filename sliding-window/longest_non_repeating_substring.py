# brute

def longest(string):
    n = len(string)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            if string[j] not in seen:
                seen.add(string[j])
                max_len = max(max_len,j-i+1)
            else:
                break
    return max_len

string = "aaabcc"
print(longest(string))

# TC - O(n x n)
# SC - O(n)

def longest(string):
    l = 0
    max_len = 0
    n = len(string)
    dist = {}

    for r in range(n):
        cur_str = string[r]
        if cur_str not in dist:
            dist[cur_str] = 0
        
        dist[cur_str]+=1

        while dist[cur_str] > 1:
            left = string[l]
            dist[left]-=1
            l+=1

            if dist[left] == 0:
                del dist[left]

        max_len = max(max_len,r-l+1)
    
    return max_len

string = "aabccbb"
print(longest(string))

# TC - O(n + n)
# SC - O(n)


# another solution - with TC - O(n)


def longest(string):
    l = 0
    max_len = 0
    n = len(string)
    dist = {}

    for r in range(n):
        cur_char = string[r]
        if cur_char in dist:
            l = max(l,dist[cur_char]+1)
        dist[cur_char] = r
        max_len = max(max_len,r-l+1)
    
    return max_len

string = "aabccbb"
print(longest(string))

# TC - O(n)
# Sc - O(n)



# using hashing

def longest(string):
    max_len = 0
    for i in range(len(string)):
        hash = [0]*255

        for j in range(i,len(string)):
            if hash[ord(string[j])] == 1:
                break
            max_len = max(max_len,j-i+1)
            hash[ord(string[j])] = 1
    return max_len

string = "aabccbb"
print(longest(string))

# TC - O(n x n)
# SC - O(255)


# optimal solution

def longest(string):
    max_len = 0
    hash = [-1]*255
    l = 0
    n = len(string)
    for r in range(n):
        if hash[ord(string[r])] != -1:
            if hash[ord(string[r])] >= l:
                l = hash[ord(string[r])] + 1
            
        max_len = max(max_len,r-l+1)
        hash[ord(string[r])] = r

    return max_len

string = "aabccbb"
print(longest(string))

# TC - O(n)
# SC - O(255)