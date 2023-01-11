from collections import deque

n = int(input())

a = list(map(int,input().split()))

q = int(input())

query = deque()

for i in range(q):
    q_i = list(map(int,input().split()))
    query.append(q_i)
    
for i in range(q):
    q_i = query.popleft()
    if q_i[0] == 1:
        a[q_i[1]-1] = q_i[2]
    else:
        print(a[q_i[1]-1])