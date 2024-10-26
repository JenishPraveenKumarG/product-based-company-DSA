# brute force

def sec_largest(arr):
    arr.sort()
    return arr[-2]

arr = [1,2,3,4,5]
print(sec_largest(arr))

# TC - O(nlogn)
# SC - O(1)


# what if elements are repeated example arr = [1 , 2 , 3, 4, 5, 5]

def sec_largest(arr):
    n = len(arr)-1 
    for i  in range(n-1, -1, -1):
        if arr[i] != arr[n]:
            return arr[i]
    return 0

arr = [1,1,2,2,3,4,4,4]
print(sec_largest(arr))    



# Better solution
    # first pass largest and then comparing each values weather it is greater than smallest and less than largest
    # smallest = -inf



def sec_largest(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i

    slargest = 0
    for i in arr:
        if i > slargest and i!=largest:
            slargest = i
    return slargest

arr = [1,1,2,2,3,4,4,4]
print(sec_largest(arr))   

# TC O(n+n)
# SC O(1)


# Optimal solution

def sec_largest(arr):
    largest = 0
    slargest = 0

    for i in arr:
        if i > largest:
            slargest = largest 
            largest = i

    return slargest

arr = [1,1,2,2,3,4,4,4]
print(sec_largest(arr))   