from collections import deque

n = int(input())

x = sorted(list(map(int,input().split())))

print(float(sum(x[n:4*n])/(3*n)))
