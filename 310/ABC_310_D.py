import itertools, more_itertools

N, T, M = map(int, input().split())

conditions = set()

d = [i+1 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    conditions.add(str(a)+str(b))

l = list(more_itertools.powerset(d))[1:]

m = []
for h in l:
    h_list = list(h)
    m.append(''.join(map(str, h_list)))

print(m)
# r = []
# for i in range(1,N+1):
#     r += list(itertools.combinations(m, i))

# ans = 0
# teams = set()

# for i in range(N):
#     for j in range(T):
    