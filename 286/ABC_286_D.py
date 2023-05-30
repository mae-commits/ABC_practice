N, X = map(int, input().split())

# 目的の金額を bit で管理
s = 1 << X

for _ in range(N):
    a, b = map(int, input().split())
    # 硬貨 a で支払える金額をbitで保持
    for _ in range(b):
        s |= s >> a

print("Yes" if s & 1 else "No")