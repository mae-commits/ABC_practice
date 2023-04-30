H, W = map(int, input().split())

C = list(list(input()) for i in range(H))

N = min(H, W)

S = [0 for i in range(N+1)]

# 中心のマーク探し
for i in range(1,H-1):
    for j in range(1,W-1):
        # 条件を満たさない場合は次の候補へ
        if C[i][j] != '#':
            continue
        # 角のグリッドが#となるので、グリッドの範囲内に収まるように設定
        n = min(i,H-1-i,j, W-1-j)
        size = 0
        for k in range(1, n+1):
            if C[i + k][j + k] == '#' and C[i + k][j - k] == '#' and C[i - k][j + k] == '#' and C[i - k][j - k] == '#':
                size += 1
            else:
                break
        S[size] += 1
        
print(*S[1:])