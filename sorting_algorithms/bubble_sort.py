# bubble sort - pushes the maximum to the last
arr = [4,3,2,1]

n = len(arr)

for i in range(n-1,-1,-1):
    for i in range(i):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        

print(arr)