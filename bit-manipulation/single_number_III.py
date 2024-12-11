# brute solution will be using a mpp and storing all the values that appears once


def single_number(arr):
    xorr = 0
    for i in arr:
        xorr ^= i
    
    right_most = (xorr & (xorr - 1)) ^ xorr

    b1 = 0
    b2 = 0

    for i in arr:
        if i & right_most:
            b1 = b1 ^ i
        else:
           b2 = b2 ^ i
    
    return [b1,b2]

arr = [4,4,2,3,3,5,5,9,7,7]
print(single_number(arr))

# TC - O(2n)
# SC - O(1)