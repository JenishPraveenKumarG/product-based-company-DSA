# naive brute solution

def bs(arr,target):
    first = -1
    last = -1
    n = len(arr)
    for i in range(n):
        if arr[i] == target and first == -1:
            first = i
        elif arr[i] == target and last != first:
            last = i
        else:
            continue
    return [first,last]



arr = [2,4,6,8,8,8,11,13]
target = 8
print(bs(arr,target))

# TC - O(n)
# SC - O(1)

# optimal solution using binary search

def lower_bound(arr,target):
    low = 0
    high = len(arr) - 1
    ans = 0

    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upper_bound(arr,target):
    low = 0
    high = len(arr) - 1
    ans = 0

    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans-1

arr = [2,4,6,8,8,8,11,13]
target = 8
lb = lower_bound(arr,target)
up = upper_bound(arr,target)

if lb == len(arr) or arr[lb]!=target:
    print([-1,-1])
else:
    print([lb,up])


# TC - O(2*log(base2)n)

# traditional binary search --- one for first and then another for last

def first_occurance(arr,target):
    low = 0
    high = len(arr)-1
    ans = 0

    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def last_occurance(arr,target):
    low = 0
    high = len(arr)-1
    ans = 0

    while low <= high:
        mid = (low + high)//2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans-1

arr = [2,4,6,8,8,8,11,13]
target = 8
fo = first_occurance(arr,target)
lo = last_occurance(arr,target)
if arr[fo] == target and arr[lo] == target:
    print([fo,lo])
else:
    print([-1,-1])
