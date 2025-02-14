def non_overlapping(meet):

    '''same like find the meetimg within the range and return the length - the n_meetings possible'''
    meet.sort(key=lambda x: x[1])  # Sort intervals by their end times
    n = len(meet)
    cnt = 0
    end_limit = meet[0][1]
    for i in range(1, n):
        if meet[i][0] < end_limit:
            cnt += 1
        else:
            end_limit = meet[i][1]
    return cnt

arr = [[0,5],[5,9],[5,7],[1, 2], [3, 4], [8, 10], [12, 16]]
print(non_overlapping(arr))

# TC - O(nlogn) + O(n)
# SC - O(1)