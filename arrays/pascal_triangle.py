
def pascal_element(n,r):
    ans = 1
    for i in range(0,r):
        ans *= n-i
        ans//=i+1
    return ans


def pascal_triangle(r,c):
    ans = []
    for row in range(1,r):
        temp = []
        for col in range(1,row+1):
            val = pascal_element(row-1,col-1)
            temp.append(val)
        ans.append(temp)
    return ans

print(pascal_triangle(6,6))

# TC - O(n**3)
# SC - O(n)


# use generate row - optimal solution


def generate_row(row):
    ans = 1
    temp = []
    temp.append(ans)

    for col in range(1,row):
        ans*=row-col
        ans//=col
        temp.append(ans)
    return temp

def pascal_triangle(n):
    ans = []

    for i in range(1,n+1):
        temp = generate_row(i)
        ans.append(temp)
    return ans

print(pascal_triangle(4))