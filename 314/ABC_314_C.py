from collections import deque

N, M = map(int, input().split())

S = input()

C = list(map(int, input().split()))

colorlist = [deque([]) for i in range(M+1)]
ans = ""


for i in range(N):
    colorlist[C[i]].append(S[i])

for i in range(M):
    i_first = colorlist[i+1].pop()
    colorlist[i+1].appendleft(i_first)

for i in range(N):
    color = C[i]
    letter = colorlist[color].popleft()
    ans+=letter
    
print(ans)