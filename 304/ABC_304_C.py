class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

N, D = map(int, input().split())
D_square = D ** 2

coordinates = [[0, 0]]

for i in range(N):
    coordinates.append(list(map(int, input().split())))

UF = UnionFind(N+1)

for i in range(1, N):
    ith_index = coordinates[i]
    for j in range(i+1, N+1):
        jth_index = coordinates[j]
        if  (ith_index[0] -jth_index[0]) ** 2 + (ith_index[1] - jth_index[1]) ** 2 <= D_square:
            UF.unite(i, j)

for i in range(1, N+1):
    if UF.issame(1, i):
        print("Yes")
    else:
        print("No")