# brute solution

def sub_array_ranges(arr):
    cnt = 0
    n = len(arr)
    for i in range(n):
        maxi = arr[i]
        mini = arr[i]
        for j in range(i+1,n):
            maxi = max(arr[j],maxi)
            mini = min(mini,arr[j])
            cnt += maxi - mini
    
    return cnt 

arr = [1,4,3,2]
print(sub_array_ranges(arr))

# TC - O(n**2)
# SC - O(1)
