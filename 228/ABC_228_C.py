from collections import deque
from email.mime import base
from operator import truediv

n,k = map(int, input().split())
p = deque(list(map(int,input().split())) for i in range(n))
scores = []

for i in range(n):
    p_i = p.popleft()
    scores.append(sum(p_i))

scoresSort = sorted(scores,reverse=True)

basePoint = scoresSort[k-1]

for i in range(n):
    if (scores[i] - basePoint) >= -300:
        print('Yes')
    else:
        print('No')