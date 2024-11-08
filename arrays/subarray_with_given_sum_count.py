# Brute solution

def count_subarray(arr,val):
    sub_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum+=arr[k]
            if sum == val:
                sub_count+=1
    return sub_count

arr = [1,2,3,-3,1,1,1,4,2,-3]
val = 3
print(count_subarray(arr,val))

# TC - O(n**3)
# SC - O(1)

# Better solution

def count_subarray(arr,val):
    sub_count = 0
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            if sum == val:
                sub_count+=1
    return sub_count

arr = [1,2,3,-3,1,1,1,4,2,-3]
val = 3
print(count_subarray(arr,val))

# TC - O(n**2)
# SC - O(1)


# Optimal solution


def count_subarray(arr,val):
    sub_count = 0
    map = {}
    n = len(arr)
    presum = 0
    map[presum] = 1
    for i in range(n):
        presum += arr[i]
        rem = presum - val
        if rem in map:
            sub_count+=map[rem]
        if presum in map:
            map[presum]+=1
        else:
            map[presum]= 1
    

    return sub_count

arr = [1,2,3,-3,1,1,1,4,2,-3]
val = 3
print(count_subarray(arr,val))

# TC - O(n)
# SC - O(n)