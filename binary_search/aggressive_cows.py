def canweplace(arr,dist,cows):
    cnt_cows = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last >= dist:
            cnt_cows+=1
            last = arr[i]
    
    if cnt_cows >= cows:
        return True

    return False
    



def aggressive_cows(arr,cows):
    arr.sort()
    mini = min(arr)
    maxi = max(arr)
    for i in range(1,maxi-mini+1):
        if canweplace(arr,i,cows) == True:
            continue
        else:
            return i-1


arr = [0,3,4,7,10,9]
cows = 4
print(aggressive_cows(arr,cows)) 

# TC - O(nlogn) + O(maxi-mini) + O(n)
# SC - O(1)

# appplying binary search

def aggressive_cows(arr,cows):
    arr.sort()
    n = len(arr)
    low = 0
    high = arr[n-1] - arr[0]

    while low <= high:
        mid = (low + high)//2
        if canweplace(arr,mid,cows):
            low = mid + 1
        else:
            high = mid - 1
    
    return high


arr = [0,3,4,7,10,9]
cows = 4
print(aggressive_cows(arr,cows)) 

# TC - O(nlogn) + O(log2maxi-mini) + O(n)
# SC - O(1)