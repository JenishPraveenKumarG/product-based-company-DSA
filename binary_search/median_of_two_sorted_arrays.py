def median(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    arr = []
    while i<n1 and j <n2:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i<n1:
        arr.append(arr1[i])
        i+=1
    while j<n2:
        arr.append(arr2[j])
        j+=1
 
    n = len(arr)
    if n%2 != 0:
        mid = n//2
        return arr[mid]
    else:
        mid1 = n//2
        mid2 = (n//2)-1
        return (arr[mid1] + arr[mid2])//2

arr1 = [1,3,4,7,10,11]
arr2 = [2,3,6,15]
print(median(arr1,arr2))

# TC - O(n1 + n2)
# SC - O(n1 + n2)

# we just need to find the 2 elements thats it

def median(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    index1 = n//2
    index2 = (n//2)-1
    i = 0
    j = 0
    cnt = 0
    index2ele = index1ele = 0
    while i<n1 and j<n2:
        if arr1[i] <= arr2[j]:
            if cnt == index1:
                index1ele = arr1[i]
            if cnt == index2:
                index2ele = arr1[i]
            cnt+=1
            i+=1
        else:
            if cnt == index1:
                index1ele = arr2[j]
            if cnt == index2:
                index2ele = arr2[j]
            cnt += 1
            j+=1
    
    while i<n1:
        if cnt == index1:
            index1ele = arr1[i]
        if cnt == index2:
            index2ele = arr1[i]
        cnt+=1
        i+=1
    while j<n2:
        if cnt == index1:
            index1ele = arr2[j]
        if cnt == index2:
            index2ele = arr2[j]
        cnt+=1
        j+=1
    
    if n%2 == 0:
        return (index1ele + index2ele)//2
    else:
        return index1ele

arr1 = [1,3,4,7,10,11]
arr2 = [2,3,6,15]
print(median(arr1,arr2))

# TC - O(n1+n2)
# SC - O(1) since we are not using any extra space here


# Optimising this one

# using symmetry where we will find the right and left half containing total number of elements from first and second array
# we will find greatest from the left half and smallest from the right half

def median(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    if n1>n2:
        return median(arr2,arr1)
    low = 0
    high = n1
    left = (n1 + n2 +1)//2
    while low<=high:
        mid1 = (low + high)//2
        mid2 = left - mid1
        
        l1,l2 = float('-inf'),float('-inf')
        r1,r2 = float('inf'),float('inf')

        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        
        if mid1 - 1 >= 0:
            l1 = arr1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = arr2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n%2 == 1:
                return max(l1,l2)
            return (max(l1,l2) + min(r1,r2))//2
        
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


    

arr1 = [2,4]
arr2 = [1,3,4]
print(median(arr1,arr2))

# TC - O(min(log2n1, log2n2))


