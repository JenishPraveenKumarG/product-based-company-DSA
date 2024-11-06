def leaders(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        leader = True
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            ans.append(arr[i])
    return ans

arr = [10,22,12,3,0,6]
print(leaders(arr))

# TC - O(n**2)
# SC - O(n) to store the answer 



# Optimal solution

def leaders(arr):
    maxi = float('-inf')
    n = len(arr)
    ans =[]
    for i in range(n-1,-1,-1):
        if arr[i] > maxi:
            ans.append(arr[i])
            maxi = arr[i]
    return ans


arr = [10,22,12,3,0,6]
print(leaders(arr))

# TC - O(n)
# SC - O(n) to store the answer 