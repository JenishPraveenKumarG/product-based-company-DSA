def minimise_max_distance(arr,k):
    n = len(arr)
    how_many = [0]*(n-1)
    for gas in range(1,k+1):
        max_section = -1
        max_index = -1

        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            section_length = diff / (how_many[i]+1)
            if section_length > max_section:
                max_section = section_length
                max_index = i
        how_many[max_index] += 1

    max_ans = -1
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        section_length = diff / (how_many[i]+1)
        max_ans = max(max_ans,section_length)
        
    return max_ans

arr = [1,13,17,23]
k = 5
print(minimise_max_distance(arr,k))


# TC - O(k x n)