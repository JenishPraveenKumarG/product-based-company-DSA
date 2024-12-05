''' Function that calls itself is know as recursion'''

# we need a base case to sop the recursion or else it runs infinite times

'''def func(cnt):
    cnt += 1

    print(cnt)
    func(cnt)

func(0)'''


def func(cnt):
    if cnt == 3:
        return
    cnt +=1 
    print(cnt)
    func(cnt)

if __name__ == "__main__":
    cnt = 0
    func(cnt)


    