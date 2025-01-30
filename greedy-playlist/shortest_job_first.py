def shortest_job(arr):
    arr.sort()
    n = len(arr)
    wait_time = time = 0
    for i in range(n):
        wait_time += time
        time += arr[i]
    
    # return the average 

    return wait_time//n

arr = [4,3,7,1,2]
print(shortest_job(arr))

# TC - O(nlogn) + O(n)
# SC - O(1)