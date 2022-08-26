from collections import deque

N = int(input())

mydict = {}

S = deque(input() for i in range(N))

for i in range(len(S)):
    S_i = S.popleft()
    if S_i not in mydict:
        mydict[S_i] = 1
        print(S_i)
    else:
        mydict[S_i] += 1
        print(S_i + "(" + str(mydict[S_i]-1) + ")")