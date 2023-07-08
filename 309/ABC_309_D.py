class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # 各集合の初期サイズは1とする

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]

    def get_size(self, x):
        root = self.find(x)
        return self.size[root]

    def set_root(self, x, root):
        self.parent[x] = root
        self.size[root] += self.size[x]
        self.size[x] = 0

 
N_1, N_2, M = map(int, input().split())
    
if __name__ == '__main__':
    ins = UnionFind(N_1+N_2+1)
    for i in range(M):
        a, b = map(int, input().split())
        if a == 1:
            ins.union(a, b)
            ins.set_root(b, 1)
        elif a == N_1+N_2+1 or b == N_1+N_2+1:
            ins.union(a, b)
            ins.set_root(a, N_1+N_2+1)
        else:
            ins.union(a, b)
    print(ins.get_size(1), ins.get_size(7))
    

    