A = list(map(int, input().split()))
sum_A = 0

for i in range(len(A)):
    sum_A += A[i] * 2 ** i

print(sum_A)