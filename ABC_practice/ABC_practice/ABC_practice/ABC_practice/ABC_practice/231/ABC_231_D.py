import sys
from collections import deque

N,M = map(int,input().split())
A_B = sorted(deque(sorted([map(int,input().split())]) for i in range(M)))
line = [0 for i in range(N+1)]

for i in range(M):
    a_b_i = A_B.popleft()
    a = a_b_i[0]
    b = a_b_i[1]
    line[a] += 1
    line[b] += 1
