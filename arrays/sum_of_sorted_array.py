# Brute force solution

def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([x**2 for x in nums])


# optimised and expcted solution to solve in a 1 to 1 interview


def sortedSquares(self, nums: List[int]) -> List[int]:
    l = 0
    r = len(nums)-1
    res = [0]*(r+1)
    n = r
    while l<=r:
        if nums[l]**2 < nums[r]**2:
            res[n] = nums[r]**2
            n-=1
            r-=1
        else:
            res[n] = nums[l]**2
            n-=1
            l+=1
    return res
