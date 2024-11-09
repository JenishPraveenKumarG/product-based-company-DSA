def four_sum(arr,target):
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l] == target:
                        temp = [arr[i],arr[j],arr[k],arr[l]]
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
    return sorted(ans)

arr = [1,0,-1,0,-2,2]
target = 0
print(four_sum(arr,target))

# TC - O(n**4) + O(nlogn)
# SC - O(target) only to store the ans

# better solution

def four_sum(arr,target):
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            hashset = set()
            for k in range(j+1,n):
                sum = arr[i]+arr[j]+arr[k]
                fourth = target - sum
                if fourth in hashset:
                    temp = [arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)
                hashset.add(arr[k])
    return sorted(ans)

arr = [1,0,-1,0,-2,2]
target = 0
print(four_sum(arr,target))


# TC - O(n**3) * O(target_sum_answer log target_sum_array) to sort the array
# SC - O(target sum) which is used to store the answer 
#       and O(quads) for look up


# optimal approach


def four_sum(arr,target):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while k<l:
                sum =  arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    temp = [arr[i],arr[j],arr[k],arr[l]]
                    if temp not in ans:
                        ans.append(temp)
                    k+=1
                    l-=1
                    while k< l and arr[k] == arr[k-1]:
                        k+=1
                    while k<l and arr[l] == arr[l+1]:
                        l-=1
                elif sum > target:
                        k+=1
                else:
                        l-=1
    return sorted(ans)

arr = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
target = 8
print(four_sum(arr,target))

# TC - o(n**3)
# SC - O(1)