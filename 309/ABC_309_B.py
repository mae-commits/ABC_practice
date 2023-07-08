N = int(input())

A = list(list(input()) for i in range(N))

B = []

if N != 2:
    for i in range(N):
        B_i = []
        if i == 0:
            B_i += A[1][0]
            B_i += A[0][0:N-1]
        elif i == N-1:
            B_i += A[N-1][1:N]
            B_i += A[N-2][N-1]
        else:
            B_i += A[i+1][0]
            B_i += A[i][1:N-1]
            B_i += A[i-1][N-1]
        B.append(B_i)
else:
    B = [[A[1][0], A[0][0]],[A[1][1], A[0][1]]]

for B_i in B:
    print(''.join(B_i))