import itertools 

n, k, d = map(int,input().split())

a = list(map(int,input().split()))

d_com = -1

for i in itertools.combinations_with_replacement(a, k):
    sum_i = sum(i)
    if sum_i >= 0 and sum_i % d == 0:
        d_com = max(sum_i, d_com)

print(d_com)