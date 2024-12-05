# print name n times

def print_name(name,n):
    if n == 0:
        return
    print(n , name)
    print_name(name,n-1)

if __name__ == "__main__":
    name = "jenish"
    n = 5
    print_name(name,n)

# TC - O(n)
# SC - O(n) internal memory

# print linearly from one to n

def print_linearly(i,n):
    if i > n:
        return
    print(i)
    print_linearly(i+1,n)

if __name__ == "__main__":
    i = 1
    print_linearly(1,n)

''' print 1 to n linearly from 1 to N without using +'''

def print_lin(i,n):
    if i<1:
        return

    print_lin(i-1,n)
    print(i)

if __name__ == "__main__":
    n = 5
    print_lin(n,n)