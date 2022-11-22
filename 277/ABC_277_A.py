import sys

n,x = map(int,input().split())

p = [0] + list(map(int,input().split()))

for i in range(n):
    if p[i+1] == x:
        print(i+1)
        sys.exit()