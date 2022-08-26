from collections import deque

N,C = map(int,input().split())

T_A = deque([map(int,input().split())] for i in range(N))
    