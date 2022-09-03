N, M = map(int,input().split())

A = list(map(int,input().split()))

dp = [[0 for i in range(N+1)] for j in range(N+1)] # dp[i][j]: Maximum sum from A[0] to A[i], and extract j numbers.
maxSum = -10 ** 19

dp[0][1] = -10 **19

for i in range(1,N+1):
    for j in range(N+1):
        if j == 0:
            dp[i][0] = 0
        elif j > i:
            dp[i][j] = -10 ** 19
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+A[i-1]*j)
    
print(dp[N][M])