# Brute solution

def union(arr1,arr2):
    seen = set()
    for i in arr1:
        seen.add(i)
    for j in arr2:
        seen.add(j)
    
    ans = []
    for i in seen:
        ans.append(i)
    
    return sorted(ans)

arr1 = [1,2,2,3,3,4,4,4,5]
arr2 = [2,4,5,6,7,8,8,8,8]

print(union(arr1,arr2))

# TC - O(n1) + O(n2)+ O(n) + O(nlogn)
# SC - O(unique elements)


# Optimal solution

def union(arr1,arr2):
    i = 0
    j = 0
    ans = []
    while i<=len(arr1)-1 and j<=len(arr2)-1:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            ans.append(arr2[j])
        else:
            j+=1
            i+=1
    
    while i<len(arr1)-1 and arr2[i] != ans[-1]:
        ans.append(arr1[i])
        i+=1
    
    while j<len(arr2)-1 and arr2[j] != ans[-1]:
        ans.append(arr2[j])
        j+=1
    
    return ans


arr1 = [1,2,2,3,3,4,4,4,5]
arr2 = [2,4,5,6,7,8,8,8,8]

print(union(arr1,arr2))


# TC - O(n1) + O(n2)
# SC - O(n1) + o(n2) - only for returning the answer


# another solution with slight modification

def union(arr1,arr2):
    i = 0
    j = 0
    ans = []
    while i<=len(arr1)-1 and j<=len(arr2)-1:
        if arr1[i] <= arr2[j]:
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i+=1
        elif arr2[j] <= arr1[i]:
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j+=1
    
    print(ans)
             
    while i<len(arr1)-1:
        if arr1[i]!= ans[-1]:
            ans.append(arr1[i])
        i+=1
    
    while j<len(arr2)-1:
        if arr2[j]!=ans[-1]:
            ans.append(arr2[j])
        j+=1
    
    return ans


arr1 = [1,2,2,3,3,4,4,4,5]
arr2 = [2,4,5,6,7,8,8,8,8]

print(union(arr1,arr2))
