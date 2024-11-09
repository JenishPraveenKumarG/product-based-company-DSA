# Brute solution

def merge_intervals(arr):
    ans = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        if ans and end<=ans[-1][1]:
            continue
        for j in range(i+1,n):
            if arr[j][0] < end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start,end])
    return ans

arr = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
print(merge_intervals(arr))

# TC - approx(O(2n)) + O(nlogn)
# SC - O(n) only to store the answer

# Optimal solution

def merge_intervals(arr):
    ans = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans

arr = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
print(merge_intervals(arr))

# TC - O(n)
# SC - O(n) to save the answer