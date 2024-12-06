# selection sort... it will select the small fix on the correct position and moves

arr = [4,3,2,1]

n = len(arr)

for i in range(n):
    mini = i
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            mini = j
    
    
    arr[i],arr[mini] = arr[mini],arr[i]

print(arr)