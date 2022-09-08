from collections import defaultdict

N,X=map(int,input().split())

DP=defaultdict(int); DP[1]=1

for _ in range(N):
    L,*A=map(int,input().split())
    E=DP.copy()
    DP=defaultdict(int)

    for a in A:
        #if X%a==0:
        for Y in E:
            DP[Y*a]+=E[Y]

print(DP[X])

# n,x = map(int,input().split())

# balls = list(list(map(int,input().split())) for i in range(n))

# count = 0