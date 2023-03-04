from collections import deque
import sys

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    q = deque([i])
    visited[i] = True
    v_cnt = 1
    e_cnt = len(g[i])
    while q:
        v = q.popleft()
        for to in g[v]:
            if visited[to]:
                continue
            visited[to] = True
            v_cnt += 1
            e_cnt += len(g[to])
            q.append(to)
    if v_cnt == e_cnt // 2:
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()
