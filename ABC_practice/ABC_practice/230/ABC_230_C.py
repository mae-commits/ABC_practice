N,A,B = map(int,input().split())

P,Q,R,S = map(int,input().split())

min_1 = min(N-A,N-B)
max_1 = max(1-A,1-B)

min_2 = min(N-A,B-1)
max_2 = max(1-A,B-N)

mass = [[] for i in range(Q-P+1)]

for i in range(P,Q+1):
    for j in range(R,S+1):
        if (i-A == j-B and (i-A >= max_1 and i-A <= min_1)) or (i-A == -(j-B) and (i-A >= max_2 and i-A <= min_2)):
            mass[i-P] += "#"
        else:
            mass[i-P] += "."

for i in range(Q-P+1):
    print(*mass[i],sep = "")