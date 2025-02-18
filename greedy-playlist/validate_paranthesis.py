def validate_parenthesis(s,idx,cnt,n):
    if cnt < 0:
        return False
    if idx == n:
        return cnt == 0
    if s[idx] == '(':
        return validate_parenthesis(s,idx+1,cnt+1,n)
    if s[idx] == ')':
        return validate_parenthesis(s,idx+1,cnt-1,n)
    
    return validate_parenthesis(s,idx+1,cnt-1,n) or  validate_parenthesis(s,idx+1,cnt+1,n) or validate_parenthesis(s,idx+1,cnt,n)

s = "(*()"
idx = 0
cnt = 0
n = len(s)
print(validate_parenthesis(s,idx,cnt,n))

# TC - O(3**n)
# SC - O(n)

# Optimized solution

def validate_parenthesis(s):
    mini = 0
    maxi = 0
    for i in range(len(s)):
        if s[i] == "(":
            mini += 1
            maxi += 1
        elif s[i] == ')':
            mini -= 1 
            maxi += 1
        else:
            mini -= 1
            maxi += 1
        if mini < 0:
            mini = 0
        if maxi < 0:
            return False
    
    return mini == 0


s1 = "()*)*()"
s2 = "(**("
s3 = "(*()"
n = len(s)
print(validate_parenthesis(s3))

# Tc - O(n)
# SC - O(1)