def binary_sum_k(arr,k):
    if k < 0:
        return 0
    n = len(arr)
    cnt = 0
    sum_ = 0
    l = 0
    for r in range(n):
        sum_+= arr[r]

        while sum_>k:
            sum_ -= arr[l]
            l+=1

        cnt += r-l+1
    
    return cnt

arr = [1,0,0,1,1,0]
k = 2
total_sum_of_values = binary_sum_k(arr,k) - binary_sum_k(arr,k-1)
print(total_sum_of_values)

# TC -  2 x O(2n)
# SC - O(1)