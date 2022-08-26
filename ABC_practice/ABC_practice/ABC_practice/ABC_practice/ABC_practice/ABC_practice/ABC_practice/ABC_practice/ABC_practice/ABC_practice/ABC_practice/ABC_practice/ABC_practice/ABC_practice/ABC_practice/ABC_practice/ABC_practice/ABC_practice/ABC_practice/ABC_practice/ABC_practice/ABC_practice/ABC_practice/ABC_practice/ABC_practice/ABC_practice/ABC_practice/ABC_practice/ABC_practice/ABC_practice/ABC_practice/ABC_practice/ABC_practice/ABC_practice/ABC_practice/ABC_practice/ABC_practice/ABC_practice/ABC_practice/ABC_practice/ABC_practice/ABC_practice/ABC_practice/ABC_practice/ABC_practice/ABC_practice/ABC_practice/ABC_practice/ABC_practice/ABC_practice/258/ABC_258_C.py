from collections import deque

N,Q = map(int,input().split())

S = input()

query = deque(list(map(int,input().split())) for i in range(Q))

P = 0

for i in range(Q):
    query_i = query.popleft()
    query_i_0 = query_i[0]
    query_i_1 = query_i[1]
    if query_i_0 == 1:
        P += query_i_1
    else:
        print(S[(query_i_1 - P)%N-1])
