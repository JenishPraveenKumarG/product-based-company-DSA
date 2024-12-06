# paramertized way

def sum_(i,sum):
    if i < 1:
        print(sum)
        return
    sum_(i-1,sum+i)

n = 3
sum_(n,0)

# TC - O(n)
# SC - O(n)


# functional recursion

def rec(n):
    if n == 0:
        return 0

    return n + rec(n-1)

print(rec(3))
