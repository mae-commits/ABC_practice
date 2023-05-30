N, X = map(int, input().split())

a, b = [0]*N, [0]*N

for i in range(N):
    a[i], b[i] = map(int, input().split())

# 各硬貨で支払える金額の正誤を記録
dp = [[False for i in range(X+1)] for j in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(X+1):
        for k in range(b[i]+1):
            if j >= a[i]*k and dp[i][j-a[i]*k]:
                dp[i+1][j] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")
