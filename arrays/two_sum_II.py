# Brute froce solution

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]

    return []

# optimised solution using 2 pointers

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers)-1

    while l<r:
        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        elif numbers[l] + numbers[r] > target:
            r-=1
        else:
            l+=1
    return []

# using hashmap

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    dict = {}
    n = len(numbers)
    for i in range(n):
        req = target - numbers[i]
        if req in dict:
            return [dict[req]+1,i+1]
        dict[numbers[i]] = i
    return []


