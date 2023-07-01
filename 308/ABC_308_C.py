from decimal import Decimal, getcontext

N = int(input())
coins = []
for i in range(N):
    A, B = map(int, input().split())
    getcontext().prec = 20
    coin = [i, Decimal(str(A))/Decimal(str(A+B))]
    coins.append(coin)
    
coins = sorted(coins, reverse=True, key=lambda x:x[1])

print(*[coins[i][0]+1 for i in range(N)])