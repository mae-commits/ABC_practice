N,M,X,T,D = map(int,input().split())

if M <= X:
    print(T - D * X + D * M)
else:
    print(T)