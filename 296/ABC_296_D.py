N, M = map(int, input().split())
ans = 10 ** 12 + 1

for a in range(1, N+1):
    b = (M+a-1)//a
    if b <= N:
        ans = min(ans, a*b)
    if a > b:
        break
if ans == 10 ** 12 + 1:
    print(-1)
else:
    print(ans)