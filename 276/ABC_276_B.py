n, m = map(int,input().split())

all_route = [[] for i in range(n+1)]

for i in range(m):
    a_i, b_i = map(int,input().split())
    all_route[a_i].append(b_i)
    all_route[b_i].append(a_i)

for i in range(n):
    length = len(all_route[i+1])
    all_route[i+1] = [length] + sorted(all_route[i+1])
    print(*all_route[i+1])