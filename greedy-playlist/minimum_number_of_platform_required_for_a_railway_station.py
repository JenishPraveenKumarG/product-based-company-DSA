def minimum_station(arrival, depart):
    n = len(arrival)
    ans = 1 
    
    for i in range(n):
        count = 1  
        for j in range(n):
            if i != j:
                if arrival[i] >= arrival[j] and arrival[i] <= depart[j]:
                    count += 1
        ans = max(ans, count)
    
    return ans

'''arrival = [10, 11, 13, 15]
depart = [12, 16, 14, 17]'''

arrival = [900,945,955,1100,1500,1800]
depart = [920,1200,1130,1150,1900,2000]
print(minimum_station(arrival, depart)) 

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# optimal solution
def minimum_station(arrival, depart):
    n = len(arrival)
    arrival.sort()
    depart.sort()
    cnt = 0
    max_cnt = 0
    i = 0
    j = 0
    while i<n:
        if arrival[i] <= depart[j]:
            i += 1
            cnt+=1
        else:
            cnt-=1
            j+=1
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt

arrival1 = [10, 11, 13, 15]
depart2 = [12, 16, 14, 17]

arrival = [900,945,955,1100,1500,1800]
depart = [920,1200,1130,1150,1900,2000]
print(minimum_station(arrival, depart)) 