
N = int(input())
coins = []
for i in range(N):
    A, B = map(int, input().split())
    coin = [i, float((A+B)/A)]
    coins.append(coin)
    
coins = sorted(coins, key=lambda x:x[1])

print(*[coins[i][0]+1 for i in range(N)])