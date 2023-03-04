from collections import defaultdict

n = int(input())

# A*B + C*D = N を満たす組 (A,B) と (C,D) の個数をカウントする
ab = defaultdict(int)
cd = defaultdict(int)
for a in range(1, n):
    for b in range(1, n):
        if a * b > n:
            break
        ab[a*b] += 1
for c in range(1, n):
    for d in range(1, n):
        if c * d > n:
            break
        cd[c*d] += 1

# A*B + C*D = N を満たす組 (A,B) と (C,D) の個数の積を足し合わせる
ans = 0
for i in range(1, n+1):
    ans += ab[i] * cd[n-i]
print(ans)
