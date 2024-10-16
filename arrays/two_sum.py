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