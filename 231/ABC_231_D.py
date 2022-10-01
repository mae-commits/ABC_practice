# import sys
# from collections import deque

# N,M = map(int,input().split())
# A_B = sorted(deque(sorted([map(int,input().split())]) for i in range(M)))
# line = [0 for i in range(N+1)]

# for i in range(M):
#     a_b_i = A_B.popleft()
#     a = a_b_i[0]
#     b = a_b_i[1]
#     line[a] += 1
#     line[b] += 1

# n, m = map(int,input().split())

# neighbor = [set() for i in range(n+1)]

# for i in range(m):
#     a, b = map(int,input().split())
#     neighbor[a].add(b)
#     neighbor[b].add(a)

# for i in range(1,n+1):
#     if len(neighbor[i]) >= 3:
#         print('No')
#         sys.exit()
        


# print('Yes')

# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n

    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 

    def same(self,a,b):
        return self.leader(a) == self.leader(b)

    def size(self,a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

# 入力の受け取り
N,M=map(int,input().split())

# UnionFind　初期化
UF=UnionFind(N+1)

# 辺の本数をカウント
count=[0]*(N+1)

# M回
for i in range(M):
    # 入力の受け取り
    A,B=map(int,input().split())
    # 辺の本数をカウント
    count[A]+=1
    count[B]+=1
    # 辺の本数が3本以上なら
    if 3<=count[A] or 3<=count[B]:
        # 「No」を出力
        print("No")
        # 終了
        exit()
    # A,Bが連結なら
    if UF.same(A,B)==True:
        # 「No」を出力
        print("No")
        # 終了
        exit()
    # そうでなければ(非連結なら)
    else:
        # A,Bに辺を張る(連結する)
        UF.merge(A,B)

# 「Yes」を出力
print("Yes")        