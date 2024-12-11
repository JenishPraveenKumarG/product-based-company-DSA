arr = [1,2,3]
n = len(arr)

subset = 1 << n
ans = []

for num in range(0,subset):
    list = []
    for i in range(0,n):
        if num & (1 << i):
            list.append(arr[i])
    ans.append(list)

print(ans)

# TC - O(n) x O(2**n)
# SC - O(n) x O(2**n)