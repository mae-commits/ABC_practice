from collections import deque

H, W, K = map(int,input().split())

C = list(input() for i in range(H))

ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        black_cnt = 0
        for ii in range(H):
            for jj in range(W):
                if (i>>ii & 1 == 0) and (j>>jj & 1 == 0):
                    if C[ii][jj] == "#":
                        black_cnt += 1
        if black_cnt == K:
            ans += 1

print(ans)