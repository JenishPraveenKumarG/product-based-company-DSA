# majority element n//3 times


def majority_element(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if arr[j] == arr[i]:
                count+=1
        if count > n//3 and arr[i] not in ans:
            ans.append(arr[i])
    return ans
    
arr = [1,1,1,3,3,2,2,2]
print(majority_element(arr))

# TC - O(n**3)
# SC - O(1)


# Better solution using hasgmap

def majority_element(arr):
    n = len(arr)
    hash = {}
    ans = []
    for i in arr:
        if i not in hash:
            hash[i] = 0
        hash[i]+=1
    
    for key,val in hash.items():
        if val > n//3:
            ans.append(key)
    return ans
    
arr = [1,1,1,3,3,2,2,2]
print(majority_element(arr))

# TC - O(n)
# SC - O(1)


# optimal solution

def majority_element(arr):
    n = len(arr)
    ele1,ele2 = 0,0
    count1,count2 = 0,0

    for i in range(n):
        if count1 == 0 and arr[i]!=ele2:
            ele1 = arr[i]
            count1+=1
        elif count2 == 0 and arr[i]!=ele1:
            ele2 = arr[i]
            count2+=1
        elif arr[i] == ele1:
            count1+=1
        elif arr[i] == ele2:
            count2+=1
        else:
            count1-=1
            count2-=1
    return [ele1,ele2]
        


arr = [1,1,1,3,3,2,2,2]
print(majority_element(arr))

# TC - O(n)
# SC - O(n)
