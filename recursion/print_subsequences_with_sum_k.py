def f(i,arr,ds,s,sum):
    if i == len(arr):
        if s == sum:
            print(ds)

        return
    
    ds.append(arr[i])
    s+=arr[i]

    f(i+1,arr,ds,s,sum)
    s-=arr[i]
    ds.pop()
    f(i+1,arr,ds,s,sum)



arr = [1,2,1]
sum = 2
ds = []
i = 0
s = 0
f(i,arr,ds,s,sum)