def solve(N, roads):
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for A, B, C in roads:
        graph[A][B] = C
        graph[B][A] = C
    
    # dp[mask][i]: ビットマスクmaskで表される集合を通って頂点iに到達するときの最大距離
    dp = [[0] * (N + 1) for _ in range(1 << N)]
    
    for mask in range(1 << N):
        for i in range(1, N + 1):
            if not (mask & (1 << (i - 1))):
                continue
            if mask == (1 << (i - 1)):
                dp[mask][i] = 0
                continue
            dp[mask][i] = float('-inf')
            for j in range(1, N + 1):
                if j == i or not (mask & (1 << (j - 1))):
                    continue
                dp[mask][i] = max(dp[mask][i], dp[mask ^ (1 << (i - 1))][j] + graph[i][j])
    
    max_sum = 0
    full_mask = (1 << N) - 1
    for i in range(1, N + 1):
        max_sum = max(max_sum, dp[full_mask][i])
    
    return max_sum

# 入力を受け取る
N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

result = solve(N, roads)
print(result)
