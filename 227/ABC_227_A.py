n, k, a = map(int,input().split())

if (a-1+k)%n != 0:
    print((a-1+k)%n)
else:
    print(n)