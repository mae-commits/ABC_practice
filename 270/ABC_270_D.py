n, k = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse = True)

get_stone = 0

stones = []

for i in A:
    if n >= i:
        for j in range(n//i):
            stones.append(i)
        n -= i * (n//i)

for i in range(len(stones)):
    if i%2 == 0:
        get_stone += stones[i]

print(get_stone)