N = int(input())

A = list(map(int, input().split()))

indices = [[i] for i in range(N+1)]

# 数列Aのi番目の数字の番号に対応する列に格納
for i in range(3*N):
    indices[A[i]].append(i+1)

f = []

for ith_index in indices[1:N+1]:
    f.append([ith_index[0], ith_index[2]])

# f(i) となるもののインデックスの順番にソート
f = sorted(f, key=lambda x:x[1])
ans = []

for f_i in f:
    ans.append(f_i[0])

print(*ans)