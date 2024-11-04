# Brute force solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

    return [-1,-1]
# This solution TC = O(n**2)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    n = len(nums)
    for i in range(n):
        req = target - nums[i]
        if req in dict:
            return [i,dict[req]]
        dict[nums[i]] = i
    return []

# TC - O(n)
# Sc - O(n)

# Optimal solution using 2 pointers

def two_sum(arr,target):
    l = 0
    r = len(arr)-1
    while l<=r:
        if arr[l] + arr[r]== target:
            return [l,r]
        elif arr[l]+arr[r] < target:
            l+=1
        else:
            r-=1
    return []

arr = [2,5,6,8,11]
target = 14
print(two_sum(arr,target))

# TC - O(n)
# SC - O(1)
