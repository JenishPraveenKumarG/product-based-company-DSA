# brute solution 

# fr equal number os posituve and negative elements

def arrange_array(arr):
    n = len(arr)
    pos = []
    neg = []

    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    
    for i in range(n//2):
        arr[2*i] = pos[i]
        arr[2*i + 1] = neg[i]

    return arr

arr = [1,-3,2,1,-5,-1]
print(arrange_array(arr))

# TC - O(n) + O(n//2)
# SC - O(2n)

# Optimal solution for equal number of positive and negatives

def arrange_array(arr):
    positive = 0
    negative = 1
    n = len(arr)
    ans = [0]*n

    for i in range(n):
        if arr[i] < 0:
            ans[negative] = arr[i]
            negative += 2
        else:
            ans[positive] = arr[i]
            positive += 2
        
    return ans

arr = [-3,-2,-1,1,0,10]
print(arrange_array(arr))


# TC - O(n)
# SC - O(n)