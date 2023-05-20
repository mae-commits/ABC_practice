import numpy as np

N, M, D = map(int, input().split())

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

ans = -1

# A を固定した際のBの各要素との差を計算
dif = np.array([])

for i in range(N):
    A_i = A[i]
    dif = B - A_i
    comp_list = np.array([A_i + B[j] for j in range(M) if abs(dif[j]) <= D])
    if len(comp_list) >= 1:
        ans = max(ans, max(comp_list))
    
print(ans)