
def pascal_element(n,r):
    ans = 1
    for i in range(0,r):
        ans *= n-i
        ans//=i+1
    return ans


def pascal_row_elements(n):
    for i in range(1,n+1):
        print(pascal_element(n-1,i-1),end = " ")

pascal_row_elements(6)

# TC O(n * r)
# SC - O(1)


# optimal solution



def pascal_row_elements(n):
    ans = 1
    print(ans, end = " ")
    for i in range(1,n):
        ans *= n-i
        ans //=i
        print(ans, end = " ")


pascal_row_elements(6)

# TC - O(n)
# SC - O(1)