N, M, X = map(int,input().split())

min_money = -1

C_A = list(list(map(int,input().split())) for i in range(N))


for i in range(1<<N):
    money = 0
    ability = [0 for i in range(M)]
    for j in range(N):
        if i >> j & 1 == 1:
            money += C_A[j][0]
            for k in range(M):
                ability[k] += C_A[j][k+1]
    if min(ability) >= X:
        if min_money != -1:
            min_money = min(money,min_money)
        else:
            min_money = money

print(min_money)