# Brute force solution

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if i not in nums:
            return i
    return i+1


# optimised solution using mathematics

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)

    sum = 0
    for num in nums:
        sum+=num
        
    n = (n*(n+1))//2
    return n-sum