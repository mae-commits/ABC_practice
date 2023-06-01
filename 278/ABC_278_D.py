from collections import defaultdict

N = int(input())

A = [0] + list(map(int, input().split()))

Q = int(input())

input_x = -1
add_x = defaultdict(int)

for i in range(Q):
    query_i = list(map(int, input().split()))
    if query_i[0] == 1:
        input_x = query_i[1]
        add_x = defaultdict(int)
    elif query_i[0] == 2:
        i_q, x_q = query_i[1], query_i[2]
        add_x[i_q] += x_q
    else:
        i_q = query_i[1]
        if input_x >= 0:
            print(input_x + add_x[i_q])
        else:
            print(A[i_q] + add_x[i_q])