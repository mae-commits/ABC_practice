n, m = map(int,input().split())

g = [[0]*n]

vis = [False]*n

def dfs(c):
    vis[c] = True
    for d in g[c]:
        if vis[d]:
            continue
        dfs(d)

for i in range(m):
    u, v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

ans = 0
for i in range(n):
    if vis[i]==False:
        ans+=1
        dfs(i)
print(ans)