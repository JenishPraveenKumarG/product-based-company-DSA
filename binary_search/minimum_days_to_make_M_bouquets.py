# brute solution

def possible(arr,day,m,k):
    
    cnt = 0
    n = len(arr)
    no_of_bo = 0
    for i in range(n):
        if arr[i] <= day:
            cnt+=1
        else:
            no_of_bo += cnt//k
            cnt = 0

    no_of_bo += cnt//k

    if no_of_bo >= m:
        return True
    else:
        return False
    
def minimum_no_of_days(arr,m,k):
    mini = min(arr)
    maxi = max(arr)

    for i in range(mini,maxi+1):
        if possible(arr,i,m,k):
            return i
    return -1

arr =[7,7,7,7,13,11,12,7]
m = 2
k = 3
print(minimum_no_of_days(arr,m,k))

# TC - O(maxi - mini) x O(n)
# SC - O(1)


# using binary search

def minimum_no_of_days(arr,m,k):
    low = min(arr)
    high = max(arr)
    ans = 0
    while low<=high:
        mid = (low + high)//2
        if possible(arr,mid,m,k) == True:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1 

    return ans
    # return low

arr =[7,7,7,7,13,11,12,7]
m = 2
k = 3
print(minimum_no_of_days(arr,m,k))

# TC - O(n) x O(log2 max-min+1)
# SC - O(1)