X, Y, N = map(int,input().split())

min_money = 10 ** 10

for i in range(N//3 + 1):
    tmp_money = (N-3*i) * X + i * Y
    min_money = min(tmp_money, min_money)
    
print(min_money)