n, m = map(int,input().split())

pinnacle = [[i] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    pinnacle[u].append(v)
    pinnacle[v].append(u)

side = set()

for i in range(n):
    side |=set(pinnacle[i])

if n > m:
    print(n-m)
else:
    print(1)