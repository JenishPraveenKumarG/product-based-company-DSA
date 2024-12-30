# brute force solution 
def remove_k_digits(digits,k):
    stack = []
    for i in digits:
        val = int(i)
        while stack and stack[-1] > val and k > 0:
            stack.pop()
            k-=1
        stack.append(val)

    while k > 0:
        stack.pop()
        k-=1

    res = ''
    while len(stack) != 0:
        res = str(stack.pop()) + res
    
    # Remove leading zeros
    res = res.lstrip('0')

    return res if res else '0'

    


digits = '1432219'
k = 3
print(remove_k_digits(digits,k))

# without converting the digits to integer

def remove_k_digits(digits, k):
    stack = []
    for i in digits:
        while stack and int(stack[-1]) > int(i) and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    while k > 0:
        stack.pop()
        k -= 1

    if len(stack) == 0:
        return '0'
    
    res = ''
    while len(stack) != 0:
        res = stack.pop() + res
    
    # Remove leading zeros
    res = res.lstrip('0')

    return res if res else '0'


digits = '1432219'
k = 3
print(remove_k_digits(digits, k))

# TC - O(n) + O(k) + O(n) + O(n) = O(3n + k)
# SC - O(n) + O(n) = O(2n)
