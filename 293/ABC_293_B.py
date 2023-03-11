from collections import deque

n = int(input())

called_name = deque(list(map(int,input().split())))

called_num = len(called_name)

name = set(i for i in range(1,n+1))

called_members = set()
for i in range(called_num):
    called_member = called_name.popleft()
    if i+1 not in called_members and called_member not in called_members:
        called_members.add(called_member)

name = name - called_members
print(len(name))
print(*name)