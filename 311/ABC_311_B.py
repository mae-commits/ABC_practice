import numpy as np

N, D = map(int, input().split())

S = np.array(list(list(input()) for i in range(N)))

free = np.array(['o' for i in range(N)])
ans = 0
continuous = True
count_continuous = 0

for i in range(D):
    S_line = S[:, i]
    if np.array_equal(S_line, free):
        continuous = True
        count_continuous += 1
    else:
        ans = max(ans, count_continuous)
        continuous = False
        count_continuous = 0

ans = max(ans, count_continuous)

print(ans)