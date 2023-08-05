N = int(input())

P = list(map(int, input().split()))

P_0 = P[0]

P = sorted(P)

if N != 1:
    if P_0 == P[-1] and P[-1] != P[-2]:
        print(0)
    else:
        print(max(P)+1-P_0)
else:
    print(0)