def stock(arr):
    profit = 0
    mini = arr[0]
    n = len(arr)
    for i in range(1,n):
        cost = arr[i] - mini
        profit = max(cost,profit)
        mini = min(mini,arr[i])
    return profit

arr = [7,1,5,3,6,4]
print(stock(arr))

# TC - O(n)
# SC - O(1)