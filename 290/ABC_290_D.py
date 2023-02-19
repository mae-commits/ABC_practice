import math

T = int(input())

for i in range(T):
    N, D, K = map(int, input().split())
    D = D%N
    if math.gcd(D,N) == 1:
        print(D*(K-1)%N)
    else:
        K -= 1
        gcd = math.gcd(N,D)
        counts = N//gcd
        loop = K // counts
        res = K % counts
        print((res*D)%N+loop)        