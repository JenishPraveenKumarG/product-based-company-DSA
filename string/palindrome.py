# brute solution

def palindrome(string):
    # reverse the string 
    copy = string[::-1]
    if copy == string:
        return True
    
    return False


string = "racecar"
print(palindrome(string))

# TC - O(n)
# Sc - O(1)

# optimal using 2 pointers

def palindrome(string):
    low,high = 0,len(string)-1

    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -=1 
    
    return True
print(palindrome(string))

# TC - O(logn)
# SC - O(1)





