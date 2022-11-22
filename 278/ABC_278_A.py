from collections import deque

n, k = map(int,input().split())

a = deque(list(map(int,input().split())))

for i in range(k):
    a.popleft()
    a.append(0)

a = list(a)

print(*a)