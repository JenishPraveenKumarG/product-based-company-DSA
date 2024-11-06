# Brute solution


def search(arr,x):
    '''To search element x+1 is in the array or not'''

    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

def longest_sequence(arr):
    longest = 1
    n = len(arr)

    for i in range(n):
        num = arr[i]
        count = 1
        while search(arr,num+1) == True:
            num +=1
            count+=1
        longest = max(longest,count)

    return longest

arr = [102,4,100,1,101,3,2,1,1]
print(longest_sequence(arr))

# TC - O(n**2)
# SC - O(1)

# Better solution


def longest_sequence(arr):
    
    arr.sort()
    longest = 1
    count = 0
    last_smallest = float('-inf')
    n = len(arr)

    for i in range(n):
        if arr[i]-1 == last_smallest:
            count += 1
            last_smallest = arr[i]
        elif arr[i] != last_smallest:
            count = 1
            last_smallest = arr[i]

        longest = max(longest,count)
    return longest

arr = [102,4,100,1,101,3,2,1,1]
print(longest_sequence(arr))

# TC - O(nlogn) - O(n)
# SC - O(1)


# Optimal solution using set

def longest_sequence(arr):
    seen = set()
    n = len(arr)
    longest = 1
    for i in arr:
        seen.add(i)
    
    for i in seen:
        if i - 1 not in seen:
            count = 1
            val = i+1
            while val in seen:
                count +=1
                val = val + 1
            longest = max(count,longest)
    return longest

arr = [102,4,100,1,101,3,2,1,1]
print(longest_sequence(arr))

# TC - O(n)
# SC - O(n)