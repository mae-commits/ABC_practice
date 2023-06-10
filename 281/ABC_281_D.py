N, K, D = map(int,input().split())

a = list(map(int,input().split()))

# a_1 ~ a_i まででj個が選ばれていて、総和をDで割ったあまりがkであるような総和の最大値 dp[i][j][k]
dp = [[[-1 for _ in range(K+1)] for _ in range(N+1)] for _ in range(D)]
dp[0][0][0] = 0

for n in range(N):
    for k in range(K+1):
        for d in range(D):
            if dp[d][n][k] >= 0:            
                # a_i を選ばない場合
                dp[d][n+1][k] = max(dp[d][n+1][k], dp[d][n][k])
                
                # a_i を選ぶ場合
                if k != K:
                    dp[(d+a[n])%D][n+1][k+1]=max(dp[d][n][k]+a[n],dp[(d+a[n])%D][n+1][k+1])
            
if dp[0][-1][-1]>=0:
    print(dp[0][-1][-1])
else:
    print(-1)