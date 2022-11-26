from collections import deque

n, m = map(int,input().split())

a = list(map(int,input().split()))

a = deque(a)

b = [i for i in range(n+1)]
