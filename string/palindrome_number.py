# brute solution

def palindrome(num):
    n = str(num)    
    n_rev = n[::-1]
    if n == n_rev:
        return True
    return False


num = 101
print(palindrome(num))

# TC - O(n) + O(n)
# SC - O(1)

# optimal solution \

def palindrome(num):
    temp = num
    num_rev = 0
    while temp:
        val = temp%10
        num_rev = num_rev*10 + val
        temp = temp//10

    if num == num_rev:
        return True
    return False

num = 1000001
print(palindrome(num))

