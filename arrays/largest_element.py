# brute force 

def largest(arr):
    arr.sort()
    return arr[-1]

arr = [5,1,7,1,9,2]
print(largest(arr))

''' TC = O(nlogn)
    SC = O(1) '''


# optimal solution

def largest(arr):
    largest = float('-inf')
    for i in arr:
       if i > largest:
           largest = i
    return largest

arr = [5,1,7,1,9,2]
print(largest(arr))

''' TC = O(nlogn)
    SC = O(1) '''

