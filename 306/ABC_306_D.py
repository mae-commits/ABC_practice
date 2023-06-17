N = int(input())

# X:毒入りかどうか 0:解毒剤入り、1:毒入り
# Y:料理のおいしさ
X, Y = [], []

# i回目の料理を食べるかどうか判断する際に
# dp[i][0]:お腹を壊していない時のおいしさの合計の最大値
# dp[i][1]:お腹を壊している時のおいしさの合計の最大値
dp = [[0, 0] for i in range(N+1)]

for i in range(1,N+1):
    X_i, Y_i = map(int, input().split())
    if X_i == 0:
        dp[i][0] = max(max(dp[i-1][0]+Y_i, dp[i-1][0]), dp[i-1][1]+Y_i)
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][0] + Y_i, dp[i-1][1])

print(max(dp[N]))