def kth_missing(arr,k):
    for i in range(len(arr)):
        if arr[i]<= k:
            k+=1
        if arr[i] > k:
            break
    return k

arr = [2,3,4,7,11]
k = 5

print(kth_missing(arr,k))

# TC - O(n)
# Sc - O(1)


def kth_missing(arr,k):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        missing = arr[mid] - (mid+1)

        if missing < k:
            low = mid + 1

        else:
            high = mid - 1
    
    return low + k
    # return high + 1 + k



#arr = [2,3,4,7,11]
arr = [4,6,7,9]
k = 3
print(kth_missing(arr,k))