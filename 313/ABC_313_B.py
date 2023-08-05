N, M = map(int, input().split())

ans = set(list(i+1 for i in range(N)))

for i in range(M):
    a, b = map(int, input().split())
    ans.discard(b)

if len(ans) == 1:
    print(list(ans)[0])
else:
    print(-1)