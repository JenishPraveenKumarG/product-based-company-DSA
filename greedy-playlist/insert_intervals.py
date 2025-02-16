def insert_intervals(arr, new_interval):
    result = []
    i = 0
    while i < len(arr) and arr[i][1] < new_interval[0]:
        result.append(arr[i])
        i += 1
    while i < len(arr) and arr[i][0] <= new_interval[1]:
        new_interval = [min(arr[i][0], new_interval[0]), max(arr[i][1], new_interval[1])]
        i += 1
    result.append(new_interval)
    result.extend(arr[i:])
    return result

arr = [[1,2],[3,4],[5,7],[8,10],[12,16]]
new_interval = [6,8]
print(insert_intervals(arr, new_interval))

# TC - O(n)
# SC - O(n) - seperate array to return the answer