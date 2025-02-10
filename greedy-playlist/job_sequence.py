class job:
    def __init__(self,id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobScheduling(self,jobs):
        jobs.sort(key = lambda x: x.profit,reverse = True)
        total_profit = 0

        cnt = 0
        max_deadline = 0
        n = len(jobs)
        for i in range(n):
            max_deadline = max(max_deadline, jobs[i].deadline)

        hash = [-1]*(max_deadline+1)

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline,0,-1):
                if hash[j] == -1:
                    hash[j] = i
                    cnt += 1
                    total_profit += jobs[i].profit
                    break
        return cnt,total_profit
        

if __name__ == "__main__":
    jobs = [job(1,4,20), job(2,1,10), job(3,1,40), job(4,1,30)]
    count,profit = Solution().jobScheduling(jobs)
    print(count,profit)


# TC - O(nlogn) + O(n) + O(max_deadline)
# SC - O(max_deadline)