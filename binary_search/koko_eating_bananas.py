# brute

def check(arr,hourly):
    total = 0
    n = len(arr)
    for i in range(n):
        total += (arr[i]//hourly)+1
    return total


def koko(arr,hour):
    ans = 1
    n = len(arr)
    for i in range(1,max(arr)):
        reqTime = check(arr,i)
        if reqTime <= hour:
            return i

arr = [3,6,7,11]
hour = 8
print(koko(arr,hour))

# TC - O(max_element) + O(n)


# using binary search

def koko(arr,hours):
    low = 0
    high = max(arr)
    ans = 0

    while low<=high:
        mid = (low + high)//2
        totalHrs = check(arr,mid)
        if totalHrs <= hours:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1
    return ans


arr = [3,6,7,11]
hour = 8
print(koko(arr,hour))

# TC - O(log2max(arr))
# SC - O(1)