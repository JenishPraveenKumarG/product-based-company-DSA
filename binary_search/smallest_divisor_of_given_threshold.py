# element must divide every element and the divison must be lesser than the threshold and we must find the minimum value

# brute solution


import math
def small_divisor(arr,thresh):
    maxi = max(arr)
    n = len(arr)

    for i in range(1,maxi+1):
        sum = 0
        for j in range(n):
            sum += math.ceil(arr[j]/i)
        if sum < thresh:
            return i
    return -1

arr = [1,2,5,9]
threshold = 6
print(small_divisor(arr,threshold))

# using binary search

def sum_of_d(arr,d):

    n = len(arr)
    sum = 0
    for i in range(n):
        sum += math.ceil(arr[i]/d)
    return sum


def small_divisor(arr,thresh):
    low = 0
    high = thresh
    while low <= high:
        mid = (low + high)//2
        if sum_of_d(arr,mid) < thresh:
            high = mid - 1
        else:
            low = mid + 1
    return low


# either you can store the answer in the variable and you can return or either low or high will be pointing the answer

arr = [1,2,5,9]
threshold = 6
print(small_divisor(arr,threshold))

# TC - O(log2 max) x O(n)