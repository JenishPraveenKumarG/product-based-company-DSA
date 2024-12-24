# brute solution

def check_anagram(str1,str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    return s1 == s2

s1 = 'ate'
s2 = 'eat'
print(check_anagram(s1,s2))

# TC - O(nlog) + O(nlogn)
# SC - O(1)


# better solution using hashing

def check_anagram(str1,str2):
    mpp = {}
    for i in str1:
        if i not in mpp:
           mpp[i] = 0
        mpp[i]+=1

    for i in str2:
        mpp[i] -= 1
        if mpp[i] == 0:
            del mpp[i]
    
    '''for key,val in mpp.items():
        if val!=0:
            return False
    return True'''

    if len(mpp) == 0:
        return True
    return False
    

s1 = 'ate'
s2 = 'eat'
print(check_anagram(s1,s2))

# TC - O(2n)
# SC - O(n)

# using array 

def check_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    arr = [0]*26

    for i in str1:
        arr[ord(i)-ord('a')] += 1
    
    for i in str2:
        arr[ord(i)-ord('a')] -= 1
    
    for val in arr:
        if val != 0:
            return False
    return True
    

s1 = 'ate'
s2 = 'eat'
print(check_anagram(s1,s2))
