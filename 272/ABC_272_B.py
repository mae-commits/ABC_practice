import sys

n,m = map(int,input().split())

members = [set([]) for i in range(n+1)]

for i in range(m):
    ith_members = list(map(int,input().split()))
    for j in ith_members[1:]:
        members[j] |= set(ith_members[1:])

# print(members)
for i in range(1,n+1):
    if len(members[i]) != n:
        print('No')
        sys.exit()

print('Yes')