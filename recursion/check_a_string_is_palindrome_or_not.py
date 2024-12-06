def check(string,l,r):
    if l >= r:
        return True
    if string[l]!=string[r]:
        return False
    
    return check(string,l+1,r-1)

string = 'raceecar'
l = 0
r = len(string)-1
print(check(string,l,r))

def check_pal(string,i,n):
    if i>=n//2:
        return True
    # print(string[i],string[n-i-1])
    if string[i] != string[n-i-1]:
        return False
    
    return check_pal(string,i+1,n)

string = 'raceecar'
n = len(string)
print(check_pal(string,0,n))

# TC - O(n)
# SC - O(n)