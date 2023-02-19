from collections import deque as d

N, K = map(int,input().split())

S = list(input())

T = ''

num = 0

for desire in S:
    if desire == 'o' and num < K:
        T+=desire
        num+=1
    else:
        T+='x'

print(T)
            