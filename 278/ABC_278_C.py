from collections import defaultdict

n,q = map(int,input().split())
data = defaultdict(set)

for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1:
        data[a].add(b)
    elif t == 2:
        data[a].discard(b)
    else:
        if data[a].issuperset({b}) and data[b].issuperset({a}):
            print("Yes")
        else:
            print("No")
