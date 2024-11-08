def pascal_element(row,col):
    n = row-1
    r = col-1
    n_fact = 1
    for i in range(1,n+1):
        n_fact *= i
    
    r_fact = 1
    for i in range(1,r+1):
        r_fact *= 1
    
    n_r_fact = 1
    n_r = n-r
    for i in range(1,n_r):
        n_fact *= i

    return n_fact//(n_r_fact * r_fact)

print(pascal_element(4,2))

# TC - O(row) + O(col) + O(row-col)
# SC - O(1)

# optimal solution



def pascal_element(row,col):
    n = row
    r = col
    ans = 1
    for i in range(col):
        ans *= n-i
        ans //= i+1
    
    return ans

print(pascal_element(4,2))

# TC - O(r)
# SC - O(1)