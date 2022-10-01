n, x, y = map(int,input().split())

# Resister the connecting pinnacles
# If connect[1] = [2,3,4], you can go from pinnacle 1 to those of 2, 3, and 4

connect = [[] for i in range(n+1)]

for i in range(n-1):
    # Receive inputs
    u, v = map(int,input().split())
    # Resister the pinnacles that connect each pinnacle
    connect[u].append(v)
    connect[v].append(u)
    
# The dustance from the pinnacle X
dist = [-1]*(n+1)

dist[x] = 0

from collections import deque
que = deque()

que.append(x)

# Repeat the manipuration until the length of que is equal to 0
while 0 < len(que):
    # Extract the pinnacle from the leftside of the que
    now = que.popleft()
    # About the pinnacles which you can go from the pinnacle you are now
    # to: the pinnacles ypu can go from the pinnacle you are now
    for to in connect[now]:
        if dist[to] == -1:
            # Resister the distances
            dist[to] = dist[now] + 1
            # Append 'to' the que
            que.append(to)
            
# Answer
ans = deque()


count = dist[y]

now=y

while 0<count:
    # Append the pinnacles where you are now to the left side of the answer
    ans.appendleft(now)
    
    # The pinnacles which you can go to from the one where you are
    for to in connect[now]:
        # If you find the pinnacle whose distance is (count -1)
        if dist[to] == count-1:
            # Minus the count by 1
            count -= 1
            # Move the pinnacle 'to'
            now=to

# Append x to the leftside of the answer
ans.appendleft(x)

# Output the answer (with *, you can output the list without braces)
print(*ans) 


