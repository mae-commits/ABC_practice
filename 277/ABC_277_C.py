from collections import deque

n, m = map(int,input().split())

a = sorted(list(map(int,input().split())))

a = deque(a)
continuous_sum = []

a_sum = sum(a)

