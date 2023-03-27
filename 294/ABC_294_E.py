L, N, M = map(int,input().split())

# 1行目の入力
A = list(list(map(int,input().split())) for _ in range(N))

# 2行目の入力
B = list(list(map(int,input().split())) for _ in range(M))

# 条件を満たす組の数をカウント
ans = 0

# 1,2 行目それぞれのブロック
i, j = 0, 0

# 各行で考えている部分のグループまでの列数を記録
p, q = 0, 0

while i < N and j < M:
    # グループの先頭要素が一致している場合、
    # 一致部分の長さを計算
    if A[i][0] == B[j][0]:
        ans += min(p + A[i][1], q + B[j][1]) - max(p, q)
    # 1行目のブロックの最後の列が2行目のブロックの最後の列よりも右側にある場合
    # 1行目は次のブロックに移行
    if p + A[i][1] < q + B[j][1]:
        p += A[i][1]
        i += 1
    # 逆の場合は2行目を次のブロックに移行
    else:
        q += B[j][1]
        j += 1
    # 同時に現在のブロックが終了してしまっている場合に関しては、
    # 次のループでそれぞれブロックが変わるので条件分けする必要がない

print(ans)