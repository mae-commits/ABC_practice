N = int(input())

ans = []
A = []
C_min = 38

for i in range(N):
    C_i = int(input())
    A_i = [C_i, i+1] + list(map(int, input().split()))
    A.append(A_i)

X = int(input())

A = sorted(A)

for i in range(N):
    C_i, num, A_i = A[i][0], A[i][1], set(A[i][2::])
    if X in A_i and C_i == min(C_i, C_min):
        ans.append(num)
        C_min = C_i
    elif C_i > C_min:
        break

print(len(ans))
print(*ans)