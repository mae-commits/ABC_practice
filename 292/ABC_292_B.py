N, Q = map(int,input().split())

event = list(list(map(int,input().split())) for i in range(Q))

judge = [0 for i in range(N+1)]

for query_i in event:
    if query_i[0] == 1:
        judge[query_i[1]]+=1
    elif query_i[0] == 2:
        judge[query_i[1]]+=2
    else:
        if judge[query_i[1]]>=2:
            print("Yes")
        else:
            print("No")