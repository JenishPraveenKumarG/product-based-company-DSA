def check(s):
    stack = []
    for i in s:
        if i == '[' or i == '{' or i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            val = stack.pop()
            if (i == ']' and val == '[') or (i == '}' and val == '{') or (i == ')' and val == '('):
                continue
            else:
                return False
    
    return len(stack) == 0

s = "()[{}()]"
print(check(s))


# TC - O(n)
# SC - O(n)
