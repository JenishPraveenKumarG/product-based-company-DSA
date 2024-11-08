def three_sum(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)
    return ans

arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))

# TC - O(n**3)
# SC - O(2n)


# Better solution using arr

def three_sum(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        hash = set()
        for j in range(i+1,n):
            third = -(arr[i] + arr[j])
            if third in hash:
                temp = [arr[i],arr[j],third]
                temp.sort()
                if temp not in ans:
                    ans.append(temp)
            hash.add(arr[j])
            
    return ans

arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))

# TC - O(n**2) + O()
# SC - O(n) + O(unique triplets)


# optimal solution to get rid of the extra space


def three_sum(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        j = i+1
        k = n-1
        arr.sort()
        while j<k:
            if arr[i] + arr[j] + arr[k] < 0:
                j+=1

            elif arr[i] + arr[j] + arr[k] > 0:
                k-=1
            else:
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
                j+=1
                k-=1
                while arr[j] == arr[j-1]:
                    j+=1
                while arr[k] == arr[k-1]:
                    k-=1

    return ans



arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))

# TC - O(nlogn) + O(n * n)
# SC - O(list) only to return the answer

