N, M = map(int, input().split())

C = list(map(str, input().split()))

D = list(map(str, input().split()))

P = list(map(int, input().split()))

ans = 0

prices = {}

for i in range(M):
    prices[D[i]] = P[i+1]

for i in range(N):
    if C[i] in prices.keys():
        ans += prices[C[i]]
    else:
        ans += P[0]

print(ans)