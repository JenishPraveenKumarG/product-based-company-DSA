class meeting:
    def __init__(self,start,end, pos):
        self.start = start
        self.end = end
        self.pos = pos


class Soluton:
    def n_meet(self, start, end, n):
        meet = [meeting(start[i],end[i],i+1) for i in range(n)]
        sorted(meet, key=lambda x: (x.end, x.pos))
        ans = []
        limit = meet[0].end
        ans.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start > limit:
                limit = meet[i].end
                ans.append(meet[i].pos)

        for i in ans:
            print(i,end = " ")

if __name__ == "__main__":
    start = [1,3,0,5,8,5]
    end = [2,4,5,7,9,9]
    obj = Soluton()
    n = 6
    obj.n_meet(start,end,n)


# TC - O(nlogn) + O(n)
# SC - O(N_meetings_that_can_be_possible) only to store the answer