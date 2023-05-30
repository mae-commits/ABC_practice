class UnionFind:
    # UnionFind の初期化
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n
        self.leaders = set()
        
    # 各木構造の根の部分を設定
    def leader(self, a):
        # 同じグループに所属している番号がない場合は入力された文字そのものを返す
        if self.parent_size[a] < 0: 
            return a
        # それ以外の場合は木構造の根の部分を探す
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]
    
    # 各数字を同じグループとして保存
    def merge(self, a, b):
        # 各数字の木構造の根の部分を返す
        x, y = self.leader(a), self.leader(b)
        # 根の数字が同じ場合は木構造をいじる必要がないので何も返さない
        if x == y: 
            return 
        # それ以外の場合、木の高さを比較
        # 大小がある場合、根の数字をswap
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        # 木の高さを更新
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return 
    # 各数字の木構造の根の部分が同じかどうか判定
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    # 木の連結部分の数をカウント
    def size(self, l):
        for num in l:
            self.leaders.add(self.leader(num))
        return len(self.leaders)
    
N, M = map(int, input().split())

UF = UnionFind(N+1)
for i in range(1, M+1):
    # 入力の受け取り
    U , V = map(int, input().split())
    
    # UとVが連結であれば
    if UF.same(U, V):
        continue
    # そうでなければ
    else:
        UF.merge(U, V)

l = [i+1 for i in range(N)]

print(UF.size(l))