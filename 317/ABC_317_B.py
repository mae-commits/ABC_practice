N = int(input())

A = sorted(list(map(int, input().split())))

A_max, A_min = max(A), min(A)

all_sum = (A_max + A_min) * (A_max - A_min + 1) / 2

print(int(all_sum - sum(A)))