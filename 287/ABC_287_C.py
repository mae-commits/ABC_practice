# import sys

# n, m = map(int,input().split())

# points = [[] for i in range(n+1)]

# for i in range(m):
#     u,v=map(int,input().split())
#     points[u].append(v)
#     points[v].append(u)

# count=0
# side=0
# for i in range(n):
#     if len(points[i+1])>=3:
#         print("No")
#         sys.exit()
#     elif len(points[i+1])==2:
#         count+=1
#     elif len(points[i+1])==1:
#         side+=1
#     else:
#         print("No")
#         sys.exit()
# if count==n-2 and m==n-1 and side==2:
#     print("Yes")
# else:
#     print("No")

import sys
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(M)]

# parentsリスト
p = [-1] * N

def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x]) # 経路圧縮
    return p[x]


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    p[x] += p[y]
    p[y] = x


degree = [0] * N

for i in range(M):
    a, b = AB[i]
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1
    # 根が共通する場合にはUniteをすると閉路を形成してしまい、
    # 一直線上にならなくなるためNoと出力し終了します
    if root(a) == root(b):
        print("No")
        exit()
    # root(a)がroot(b)の親となるようにつなぎます
    unite(a, b)

if max(degree) <= 2 and M==N-1:
    print("Yes")
else:
    print("No")
