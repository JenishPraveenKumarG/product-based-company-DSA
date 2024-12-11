                                
def findSingleNumber(nums):
    ans = 0

    for bitIndex in range(32):
        cnt = 0 
        for num in nums:
            if num & (1 << bitIndex):
                cnt += 1 
        if cnt % 3 == 1:
            ans |= (1 << bitIndex)

    return ans

# Example input array
nums = [4, 4, 4, 2, 5, 5, 5]
print("Input Array:", nums)
print("Element that appears only once:", findSingleNumber(nums))
    
                                
# TC - O(32 x n)
# SC - O(1)

# optimal approach

                                
def findSingleNumber(nums):
    nums.sort()

    for i in range(1,len(nums),3):
        if nums[i]!=nums[i-1]:
            return nums[i-1]

    return nums[-1]

nums = [4, 4, 4, 2,2,2, 5]
print("Input Array:", nums)
print("Element that appears only once:", findSingleNumber(nums))
    
                                
                            
# TC - O(nlogn) + O(n//3)
# SC - O(1)



# bucketing

                                
def findSingleNumber(nums):
    ones = 0
    twos = 0

    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    
    return ones

# Example input array
nums = [4, 4, 4, 2, 5, 5, 5]
print("Input Array:", nums)
print("Element that appears only once:", findSingleNumber(nums))
    
# TC - O(n)
# SC - O(1)
                                
                            