def f(i,arr,ds,s,sum):
    if i == len(arr):
        # condition satisfied
        if s == sum:
            print(ds)
            return True
        else:
            # condition not satisfied
            return False
    
    ds.append(arr[i])
    s+=arr[i]

    if f(i+1,arr,ds,s,sum) == True:
        return True
    s-=arr[i]
    ds.pop()
    if f(i+1,arr,ds,s,sum):
        return True
    
    return False



arr = [1,2,1]
sum = 2
ds = []
i = 0
s = 0
f(i,arr,ds,s,sum)