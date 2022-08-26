class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n
        
    # Resister a and b as the same group.
    def merge(self, a, b):
        x, y=self.leader(a), self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y] 
        self.parent_size[y]=x
        return 
    
    # Confirm whether a and b belong to the same group.
    def same(self, a, b):
        # If they belong to the same group, return True; otherwise, return False.
        return self.leader(a) == self.leader(b)
    
    # Return the leader of a, if a himself is the leader, return a.
    def leader(self, a):
        if self.parent_size[a]<0: 
            return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    
    # Return the number of group which a belongs to.
    def size(self, a):
        return abs(self.parent_size[self.leader(a)])
    
    # Return all groups whose shapes are two dimentions.
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

N,M=map(int, input().split())
Uni=UnionFind(N)

for i in range(M):
    A,B=map(int, input().split())
    A-=1
    B-=1
    Uni.merge(A,B)

friends_group=Uni.groups()

friends_size=[]
for fri in friends_group:
    friends_size.append(len(fri))

print(max(friends_size))
