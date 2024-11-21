# to find the capacity ....we find the maximum weight 
# example we have 9,10 therefore the weight must be greater than than so we find the maximum weight in the weights and run till sum of all weights


def func(weights,cap):
    day = 1
    load = 0

    for i in range(len(weights)):
        if load + weights[i] > cap:
            day = day + 1
            load = weights[i]
        
        else:
            load += weights[i]
    return day


def minimum_capacity(weights,dats):
    maxi = max(weights)
    sum_val = sum(weights)
    
    for cap in range(maxi, sum_val+1):
        days_req = func(weights,cap)
        if days_req <= days:
            return cap

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(minimum_capacity(weights,days))

# TC - O(max - min) x O(n)
# SC - O(1)

# optimal solution


def minimum_capacity(weights,days):
    low = max(weights)
    high = sum(weights)

    while low<=high:
        mid = (low + high)//2
        req_days = func(weights,mid)
        if req_days <= days:
            high = mid - 1
        else:
            low - mid + 1

    return low
 
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(minimum_capacity(weights,days))