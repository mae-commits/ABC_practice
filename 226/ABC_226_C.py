from collections import deque
n = int(input())
t_k = deque(list(map(int,input().split())) for i in range(n))
need = [0 for i in range(n+1)]
timeList = [0]

for i in range(n):
    t_k_i = t_k.popleft()
    timeList.append(t_k_i[0])
    need[i+1] = t_k_i[2:]