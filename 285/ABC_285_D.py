class UnionFind:
    # UnionFind の初期化
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n
    
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

N = int(input())

UF = UnionFind(2*N+2)

# 連想配列 (defaultdict) を用意
from collections import defaultdict

# 初期値0 の連想配列
Num = defaultdict(int)

for i in range(1, N+1):
    # 入力の受け取り
    S, T = map(str, input().split())
    
    # Sに番号がまだ振られていなければ
    if Num[S] == 0:
        Num[S] = 2 * i
    # Tに番号がまだ振られていなければ
    if Num[T] == 0:
        Num[T] = 2 * i + 1
    
    # SとTが連結であれば
    if UF.same(Num[S], Num[T]):
        # ループになるので"No"
        print("No")
        # 終了
        exit()
    # そうでなければ
    else:
        UF.merge(Num[S], Num[T])

print("Yes")