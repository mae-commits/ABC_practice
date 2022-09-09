s,t,x = map(int,input().split())

if s > t:
    if x >= s or x < t:
        print('Yes')
    else:
        print('No')
elif s < t:
    if x >= s and x < t:
        print('Yes')
    else:
        print('No')