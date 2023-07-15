N, M = map(int, input().split())

goods = sorted(list(list(map(int, input().split())) for i in range(N)), reverse=True)

for i in range(N-1):
    goods_i_func = set(goods[i][2:])
    for j in range(i+1, N):
        goods_j_func = set(goods[j][2:])
        if goods[i][0] > goods[j][0] and goods_i_func <= goods_j_func:
            print('Yes')
            exit()
        elif goods[i][0] == goods[j][0] and goods_i_func < goods_j_func:
            print('Yes')
            exit()

print('No')