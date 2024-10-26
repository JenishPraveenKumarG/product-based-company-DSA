# optimised solution

def check_sort(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] <= arr[i-1]:
            return False
    return True

arr = [1,2,3,4,4,4,5]
arr2 = [1,3,2,1,3,4]

print(check_sort(arr))
print(check_sort(arr2))

# TC - O(n)
# SC - O(1)