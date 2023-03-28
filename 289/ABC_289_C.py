
# N：整数の最大値、M：集合の数

N, M = map(int, input().split())

# 集合を格納

A = []

# 集合の入力

for i in range(M):
    C = int(input())
    A_i = list(map(int, input().split()))
    A.append(A_i)

ans = 0

numbers = set()



# bit 全探索で集合の選び方を全て数え上げ

for bit in range(1 << M):
    for i in range(M):
        if bit >> i & 1:
            numbers |= set(A[i])
    if len(numbers) == N:
        ans += 1
    
    # 1つの場合分けが終わった際に初期化
    numbers = set()

print(ans)