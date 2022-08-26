N,L,R = map(int,input().split())

A = [0] + list(map(int,input().split()))

sum_A_res = min(L*N,R*N)

dif_L_i = [0]*N

min_L = 0

L_pos = 0

min_R = 0

dif_R_i = [0]*N

R_pos = 0

for i in range(1,N):
    dif_L_i = (L-A[i]) + dif_L_i
    min_L = min(min_L,dif_L_i)
    if min_L == dif_L_i:
        L_pos = i
        
for j in range(1,N):
    dif_R_i = (R - A[N-j+1]) + dif_R_i
    min_R = min(min_R,dif_R_i)
    if min_R == dif_R_i:
        R_pos = j

print(min(L*L_pos + R*R_pos + sum(A[L_pos+1:N-R_pos+1]),sum_A_res))
