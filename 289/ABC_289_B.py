class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n

    # 代表値検索
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # グループ化
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        # 同じグループのうち、最も右側の位置を代表値(親)にする
        if y>x:
            x,y=y,x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

if __name__ =="__main__":    
    N, M = [int(nm) for nm in input().split()]
    A = [int(a) for a in input().split()]
    uf = UnionFind(N)
    # レ点でつながるグループを作成
    for a in A:
        uf.union(a-1, a)
    
    # 読まれる順番を保存
    order = []
    # 前から i 番目 の整数が読まれているか、いないかの状態を管理
    ok = [False for _ in range(N)]

    for i in range(N):
        # 既に読まれていればスキップ
        if ok[i]:
            continue

        # レ が後になければそのまま読む
        if uf.parents[i] == -1:
            order.append(i+1)
        
        else:
            # ここより後ろにある位置で、最初に読まなければいけない位置
            x = uf.find(i)
            # この位置から i まで逆順に読む
            for j in range(x,i-1,-1):
                order.append(j+1)
                # 読まれた状態へ更新
                ok[j] = True
    
    print(*order)