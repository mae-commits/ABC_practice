from collections import defaultdict, deque
import numpy as np

N, K = map(int, input().split())

d = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    d[a] += b

d = np.array(sorted(d.items(), key=lambda x: x[0]))

num = np.sum(d, axis=0)[1]

len_d = len(d)

d_deque = deque(d)

days, losts = 0, 0
for i in range(len_d):
    num -= losts
    if num <= K:
        print(days+1)
        exit()
    [days, losts] = d_deque.popleft()

print(days+1)