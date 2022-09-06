# N,L,R = map(int,input().split())

# A = [0] + list(map(int,input().split()))

# sum_A_res = min(L*N,R*N)

# dif_L_i = 0

# min_L = 0

# L_pos = 0

# min_R = 0

# dif_R_i = 0

# R_pos = 0

# for i in range(1,N):
#     dif_L_i = (L-A[i]) + dif_L_i
#     min_L = min(min_L,dif_L_i)
#     if min_L == dif_L_i:
#         L_pos = i
        
# for j in range(1,N-L_pos):
#     dif_R_i = (R - A[N-j+1]) + dif_R_i
#     min_R = min(min_R,dif_R_i)
#     if min_R == dif_R_i:
#         R_pos = j

# print(min(L*L_pos +  R*R_pos + sum(A[L_pos+1:N-R_pos+1]),sum_A_res))

# 入力の受け取り
N,L,R=map(int,input().split())
A=list(map(int,input().split()))

# fの計算
# A[0]を埋める
A1=[0]+A
# fを作る(f(0)=0)
f=[0]*(N+1)

# i=1~N
for i in range(1,N+1):
    # fの計算
    f[i]=min(f[i-1]+A1[i],L*i)

# Aをひっくり返す
A=A[::-1]
# A[0]を埋める
A2=[0]+A

# gを作る(g(0)=0)
g=[0]*(N+1)

# i=1~N
for i in range(1,N+1):
    # fの計算
    g[i]=min(g[i-1]+A2[i],R*i)

# 答え
ans=10**15
# i=0~N
for i in range(N+1):
    # これまでの答えとf[i]+g[N-i]の小さい方で更新
    ans=min(ans,f[i]+g[N-i])

# 答えの出力
print(ans)