import sys

n, t = map(int,input().split())

a = [0] + list(map(int,input().split()))

a_sum = [0 for i in range(n+1)]

latest_sum = 0

for i in range(n):
    a_sum[i+1] = latest_sum + a[i+1]
    latest_sum = a_sum[i+1]

t_mod = t%latest_sum

for i in range(n):
    if t_mod < a_sum[i+1]:
        print(str(i+1) + " " + str(t_mod - a_sum[i]))
        sys.exit()