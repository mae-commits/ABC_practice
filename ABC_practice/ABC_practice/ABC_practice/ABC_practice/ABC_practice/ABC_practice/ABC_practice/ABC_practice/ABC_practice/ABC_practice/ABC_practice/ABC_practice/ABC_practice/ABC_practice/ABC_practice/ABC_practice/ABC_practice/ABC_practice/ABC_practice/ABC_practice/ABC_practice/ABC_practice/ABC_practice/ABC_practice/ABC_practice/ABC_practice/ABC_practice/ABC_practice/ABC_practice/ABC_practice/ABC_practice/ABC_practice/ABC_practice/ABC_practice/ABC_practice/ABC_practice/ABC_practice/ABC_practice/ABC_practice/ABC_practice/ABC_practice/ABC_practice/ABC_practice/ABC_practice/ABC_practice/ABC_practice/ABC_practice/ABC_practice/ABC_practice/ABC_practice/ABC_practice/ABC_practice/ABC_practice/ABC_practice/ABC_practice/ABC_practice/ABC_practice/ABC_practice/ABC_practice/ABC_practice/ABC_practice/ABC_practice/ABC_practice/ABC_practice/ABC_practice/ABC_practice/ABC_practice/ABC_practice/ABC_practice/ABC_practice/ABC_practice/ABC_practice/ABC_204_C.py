N,M = map(int,input().split())

connect = [[] for i in range(N+1)]

for i in range(M):
    A,B = map(int,input().split())
    # Append the place numbers where we can reach from the place where we are now.
    connect[A].append(B) 

from collections import deque

# Define BFS function.
def BFS(start):
    # Resister the deque objects all of whose objects are boolean values.
    # That is why we can detect which places we have already reach.
    visited=[False]*(N+1)
    # Of course, start valie becomes zero.
    visited[start]=True
    # Starting place itself can be a goal, so the initial count is 1.
    cnt=1
    que=deque()
    que.append(start)
    while 0<len(que):
        now_city= que.popleft()
        for to_city in connect[now_city]:
            # If visited[to_city] is the place where we reach for the first time,
            # mark this city to True.
            if visited[to_city] == False:
                visited[to_city]=True
                cnt+=1
                # newly append the new city as the new start points.
                que.append(to_city)
    return cnt

ans = 0

for i in range(1, N+1):
    ans+=BFS(i)

print(ans)