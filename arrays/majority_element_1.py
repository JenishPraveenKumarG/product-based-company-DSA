# element should appear more tyhan n//2 times

# Brute solution

def majority_element(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > n//2:
            return arr[i]

arr = [2,2,3,3,1,2,2]
print(majority_element(arr))

# TC - O(n*2)
# Sc - O(1)


# Better solution using hashing

def majority_element(arr):
    n = len(arr)
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 0
        count[i]+=1
    for key,val in count.items():
        if val > n//2:
            return key
    return 0

arr = [2,2,3,3,1,2,2]
print(majority_element(arr))

# TC - O(n)
# SC - O(1)


# Optimal solution - Moores voting algorithm

def majority_element(arr):
    n = len(arr)
    element = 0
    count = 0
    for i in arr:
        if count == 0:
            element = i
        if i == element:
            count+=1
        else:
            count -= 1
    
    counter = 0
    for i in arr:
        if i == element:
            counter += 1

    if counter>n//2:
        return element
    return -1

arr = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority_element(arr))


# TC - O(n)
# SC - O91