from collections import deque

Q = int(input())

S = deque(['1'])

for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        S.append(str(query[1]))
    elif query[0] == 2:
        S.popleft()
    else:
        digit_S = int("".join(S))
        print(digit_S%998244353)       