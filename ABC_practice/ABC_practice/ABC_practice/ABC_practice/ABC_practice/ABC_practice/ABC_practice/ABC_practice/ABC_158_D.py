from collections import deque

S = deque(input())

Q = int(input())

query = deque(list(map(str,input().split())) for i in range(Q))

status = False # decide whether or not the string returns.
# True: Returned, False: Not returned.

for i in range(Q):
    query_i = query.popleft()
    if query_i[0] == "1":
        if status == True:
            status = False
        else:
            status = True
    else:
        if query_i[1] == "1":
            if status == False:
                S.appendleft(query_i[2])
            else:
                S.append(query_i[2])
        else:
            if status == False:
                S.append(query_i[2])
            else:
                S.appendleft(query_i[2])

list_S = list(S)
if status == False:
    print("".join(list_S))
else:
    print("".join(list_S[::-1]))
                             