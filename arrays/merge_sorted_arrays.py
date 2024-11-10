# Brute solution 1

def merge_array(arr1,arr2):
    for i in arr2:
        arr1.append(i)
    return sorted(arr1)

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge_array(arr1,arr2))

# TC  - O(len(arr2)) + O(nlogn)
# SC - O(1)

# Brute solution 2

def merge_array(arr1,arr2):
    arr1.extend(arr2)
    return sorted(arr1)

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge_array(arr1,arr2))

# TC  - O(len(arr2)) + O(nlogn)
# SC - O(1)

# Naive solution using 2 pointers]

def merge_array(arr1,arr2):
    arr3 = []
    n1 = len(arr1)
    n2 = len(arr2)
    l1 = 0
    l2 = 0
    while l1<n1 and l2<n2:
        if arr1[l1] <= arr2[l2]:
            arr3.append(arr1[l1])
            l1+=1
        else:
            arr3.append(arr2[l2])
            l2+=1
    while l1<n1:
        arr3.append(arr1[l1])
        l1+=1

    while l2<n2:
        arr3.append(arr2[l2])
        l2+=1

    return arr3


arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge_array(arr1,arr2))

# TC - O(n + m)
# SC - O(n + m)

# optimal solution without using extra space

def merge_array(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    left = n-1
    right = 0

    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -= 1
            right +=1
        
        else :
            # arr1[left] < arr2[right]
            break

    arr1.sort()
    arr2.sort()
    return arr1,arr2


arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge_array(arr1,arr2))

# TC - O(min(n,m)) + O(nlogn) + O(mlogm)
# SC - O(1) 


# Optimal solution 2 - using gap method

# using shell sort

def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2, n, m):
    n = len(arr1)
    m = len(arr2)
    leng = n + m

    # Initial gap:
    gap = (leng // 2) + (leng % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < leng:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)





arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge_array(arr1,arr2))

# TC - 




