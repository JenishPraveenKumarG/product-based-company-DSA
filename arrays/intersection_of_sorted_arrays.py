def intersect(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    visited = [0]*n2
    i = 0
    ans = []
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and visited[j] == 0:
                ans.append(arr1[i])
                visited[j] = 1
                break
            if arr1[i] < arr2[j]:
                break

    return ans
        
arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,6,7]
print(intersect(arr1,arr2))

# TC - O(n1*n2)
# SC - O(2n)


# Optimised approach using 2 pointers

def intersect(arr1,arr2):
    ans = []
    i = j = 0
    n1 = len(arr1)
    n2 = len(arr2)
    while i<n1 and j<n2:
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1
    return ans
        

arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,6,7]
print(intersect(arr1,arr2))

# TC - O(min(n1,n2)) for best case
# TC - O(n1+n2) for the worst case

# SC - O(n) only for storing the answer