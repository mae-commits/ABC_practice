X,K,D = map(int,input().split())

if abs(X) - K*D >= 0:
    print(abs(X)-K*D)
elif (K - (X//D))%2 == 0:
    print(abs(X) - D * (abs(X)//D))
else:
    print(D - (abs(X) - D * (abs(X)//D)))
