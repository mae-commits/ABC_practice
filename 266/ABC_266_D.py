N = int(input())

snuke = list(list(map(int,input().split())) for i in range(N))

snuke_point = [[0,0,0,0,0] for i in range(snuke[N-1][0]+1)]

for i in range(N):
    snuke_point[snuke[i][0]][snuke[i][1]] = snuke[i][2]
 
# The maximum scale Takahashi can get
dp = [[-10**18 for i in range(5)] for i in range(snuke[N-1][0]+1)]

dp[0][0] = 0

# print(dp)
for i in range(1,snuke[N-1][0]+1):
    for j in range(5):
        dp[i][j] = max(dp[i-1][min(j+1,4)], dp[i-1][max(j-1,0)], dp[i-1][j]) + snuke_point[i][j]

print(max(dp[snuke[N-1][0]]))
