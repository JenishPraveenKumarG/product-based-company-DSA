start = 10
goal = 7

ans = start ^ goal
cnt = 0

for i in range(32):
    if ans & (1 << i):
        cnt += 1

print(cnt)