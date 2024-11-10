def missing_and_repeated(arr):
    repeat = -1
    missing = -1
    n = len(arr)
    for i in range(1,n):
        count = 0
        for j in range(n):
            if i == arr[j]:
                count+=1
        if count == 2:
            repeat = i
        if count == 0:
            missing = i
        if repeat != -1 and missing != -1:
            break
    
    return [missing,repeat]


arr = [4,3,6,2,1,1]
print(missing_and_repeated(arr))

# TC - O(n**2)
# SC - O(1)

# Better solution using hashing

def missing_and_repeated(arr):
    n = len(arr)
    hasharr = [0]*(n+1)
    for i in range(n):
        hasharr[arr[i]]+=1
    
    repeat = -1
    missing = -1

    for i in range(1,len(hasharr)):
        if hasharr[i] == 2:
            repeat = i
        elif hasharr[i] == 0:
            missing = i
        if repeat != -1 and missing != -1:
            break
    
    return [missing,repeat]

arr = [4,3,6,2,1,1]
print(missing_and_repeated(arr))

# TC  - O(2n)
# SC - O(n)

# optimal solution using maths


def missing_and_repeated(arr):
    n = len(arr)
    sn= (n*(n+1))//2
    s2n = (n * (n+1) * (2*n+1))//6

    s = 0
    s2 = 0
    for i in range(n):
        s += arr[i]
        s2 += arr[i]*arr[i]

    val1 = s - sn  # x - y
    val2 = s2 - s2n  # x**2 - y**2
    # val2 = (x + y) * (x - y)
    # in which we have val1 in val2

    val2 = val2//val1 # x + y
    
    x = (val1 +val2)//2
    y = x - val1

    # return x,y
    return [y,x]



arr = [4,3,6,2,1,1]
print(missing_and_repeated(arr))


# optimal 2 using xor 

# steps
'''
    1.  arr[i] ^ (1->n)
    2. find the differ aagum bit from right side
    3. put them in 2 parts -> 0's and 1's in the differ aagum bit
    4. xor the 2 parts you will get the answer
'''

def missing_and_repeated(arr):
    n = len(arr)
    xor = 0

    for i in range(n):
        xor ^= arr[i]
        xor ^= i+1
    
    bit_no = 0
    while 1:
        if xor & 1<<bit_no != 0:
            break
        bit_no += 1
    
    zero = 0
    one = 0

    for i in range(n):
        # part of 1's club
        if (arr[i] & 1<<bit_no) != 0:
            one^=arr[i]
        # part o's club
        else:
            zero^=arr[i]

    for i in range(1,n+1):
        # part of 1's club
        if (i & 1<<bit_no) != 0:
            one^=i
        # part o's club
        else:
            zero^=i
    
    count = 0
    for i in range(n):
        if arr[i] == zero:
            count+=1
    if count == 2:
        return [zero,one]
    return [one,zero]

arr = [4,3,6,2,1,1]
print(missing_and_repeated(arr))
