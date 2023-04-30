N, A, B = map(int, input().split())

C = list(map(int, input().split()))

ans_sum = A + B

for i in range(N):
    if C[i] == ans_sum:
        print(i+1)
        exit()