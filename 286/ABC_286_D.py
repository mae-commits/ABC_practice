n, x = map(int,input().split())

coins = list(list(map(int,input().split())) for i in range(n))

coins = sorted(coins)

dp = [[] for i in range(n+1)]

dp[0].append(x)

