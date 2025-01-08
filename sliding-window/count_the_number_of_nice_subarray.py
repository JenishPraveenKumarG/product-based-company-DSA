def nice(arr,k):
    if k < 0:
        return 0
    n = len(arr)
    cnt = 0
    sum_ = 0
    l = 0
    for r in range(n):
        sum_+= arr[r]%2

        while sum_>k:
            sum_ -= arr[l]%2

            l+=1

        cnt += r-l+1
    
    return cnt

arr = [1,1,2,1,1]
k = 3
total = nice(arr,k) - nice(arr,k-1)
print(total)

# TC - 2 x O(2n)
# SC - O(1)