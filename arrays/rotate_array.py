# brute force solution

def rotate(self, nums: List[int], k: int) -> None:
        
    k = k%len(nums)
    val = 0
    for i in range(len(nums)-1,-1,-1):
        if val == k:
            break
        rem = nums.pop()
        nums.insert(0,rem)
        val+=1

    return nums

# the above solution takes huge amout of time

# Expected solution/ optimised solution

def rev(self,nums,l,r):
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    return nums

def rotate(self, nums: List[int], k: int) -> None:
        
    k = k%len(nums)
    nums.reverse()
    self.rev(nums,0,k-1)
    self.rev(nums,k,len(nums)-1)
    return nums