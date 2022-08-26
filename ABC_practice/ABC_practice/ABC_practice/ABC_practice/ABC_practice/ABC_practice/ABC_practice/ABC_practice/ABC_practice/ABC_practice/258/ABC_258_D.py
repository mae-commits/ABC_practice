from collections import deque

N,X = map(int,input().split())

A_B = deque(list(map(int,input().split())) for i in range(N))

min_time = 10 ** 20

tmp_time = 0

for i in range(N):
    A_B_i = A_B.popleft()
    tmp_time += sum(A_B_i)
    re_time = A_B_i[1]
    if (i+1) > X:
        break
    else:
        repeat_time = X - (i+1)
        min_time = min(min_time, tmp_time + repeat_time * re_time)

print(min_time)
        