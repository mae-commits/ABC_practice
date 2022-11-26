import math

def time_func(floor_alpha, a, b):
    return int(a/math.sqrt(floor_alpha + 1) * 10**6) + int(b*floor_alpha*10**6)

a, b = map(int,input().split())

alpha = float(a/(2*b)) ** (float(2.0/3.0)) - 1

floor_alpha = int(alpha)

t_min = min(time_func(floor_alpha, a, b), time_func(floor_alpha+1, a, b))

print('{:.7f}'.format(t_min/10**6))
