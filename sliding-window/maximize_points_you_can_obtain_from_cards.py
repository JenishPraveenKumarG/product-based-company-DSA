def maximize(arr,k):
    lsum = 0
    rsum = 0
    n = len(arr)
    rindex = n-1
    max_sum = 0
    for i in range(k):
        lsum += arr[i]
    max_sum = lsum
    
    for i in range(k-1,-1,-1):
        lsum -= arr[i]
        rsum += arr[rindex]
        rindex -= 1

        max_sum = max(max_sum,lsum + rsum)
    return max_sum

arr = [6,2,3,4,7,2,1,7,1]
k = 4
print(maximize(arr,k))

# TC - O(2k)
# Sc - O(1)