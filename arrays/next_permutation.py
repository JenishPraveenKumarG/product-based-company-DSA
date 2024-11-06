# Brute solution - generate all the permutaton and search linearly and perint the next permutation

# TC - O(n!) * O(n)
# SC - O(1)


# optimal solution

def next_permutation(arr):
    index = -1
    n = len(arr)
    for i in range(n):
        if arr[i] < arr[i+1]:
            index = i
            break
    print(arr[index])
    if index == -1:
        l = 0
        r = len(arr)-1
        while l<r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
        return arr
    
    for i in range(n-1,index,-1):
        if arr[i] > arr[index]:
            arr[i],arr[index] = arr[index],arr[i]
            break
    
    l = index+1
    r = len(arr) - 1

    print(arr)

    while l<r:
        arr[l],arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    return arr


arr = [2,1,5,4,3,0,0]
print(next_permutation(arr))

# TC - O(n**3)
# SC - O(1)