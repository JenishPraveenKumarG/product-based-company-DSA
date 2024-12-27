# brute solution

def stock_spanner(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        cur_sum = 1
        for j in range(i-1,-1,-1):
            if arr[j] <= arr[i]:
                cur_sum += 1
            else:
                break
        maxi = max(maxi,cur_sum)
    return maxi

arr = [7,2,1,3,3,1,8]
print(stock_spanner(arr))

# TC - O(n x n)
# SC - O(1)

# optimal solution

def stock_spanner(arr):
    n = len(arr)
    maxi = 0
    stack = []
    for i in range(n):
        while stack and stack[-1][0] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            maxi = max(maxi,i-(-1))
        else:
            maxi = max(maxi,i-stack[-1][1])
        stack.append([arr[i],i])
    
    return maxi

arr = [7,2,1,3,3,1,8]
print(stock_spanner(arr))

# TC - O(2n) 
# SC - O(n)