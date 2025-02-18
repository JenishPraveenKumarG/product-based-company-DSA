class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

class Solution:
    def ks(self,w,arr,n):
        arr.sort(key = lambda x:x.value/x.weight, reverse = True)
        tot = 0
        for i in range(n):
            if arr[i].weight < w:
                tot += arr[i].value
                w -= arr[i].weight
            else:
                tot += (arr[i].value/arr[i].weight) * w
        return tot

if __name__ == "__main__":
    n = 4
    w = 90
    arr =  [Item(100,20),Item(60,10),Item(100,50),Item(200,50)]
    obj = Solution()
    ans = obj.ks(w,arr,n)
    print(ans)

# TC - o(nlogn) + O(n)
# SC - O(1)