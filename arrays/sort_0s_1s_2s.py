# brute solution

def sort(arr):
    return sorted(arr)

arr = [0,1,0,1,2,2,2,1,0,1]
print(sort(arr))

# TC - O(nlogn)
# SC - O(1)


# Better solution
# count each elements

def sort(arr):
    zeros = 0
    ones = 0
    two = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            zeros+=1
        elif arr[i] == 1:
            ones +=1
        else:
            two += 1
    for i in range(zeros):
        arr[i]=0
    for i in range(zeros,zeros+ones):
        arr[i] = 1
    for i in range(zeros+ones,len(arr)):
        arr[i] = 2
    return arr

arr = [0,1,0,1,2,2,2,1,0,1]
print(sort(arr))

# TC - o(2n)
# SC - O(1)


# Optimal solution - ducth national flag algorithm (3 pointers)

def sort(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid<=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -=1 
    return arr
  
arr = [0,1,0,1,2,2,2,1,0,1]
print(sort(arr))

# TC - O(n)
# SC - O(1)