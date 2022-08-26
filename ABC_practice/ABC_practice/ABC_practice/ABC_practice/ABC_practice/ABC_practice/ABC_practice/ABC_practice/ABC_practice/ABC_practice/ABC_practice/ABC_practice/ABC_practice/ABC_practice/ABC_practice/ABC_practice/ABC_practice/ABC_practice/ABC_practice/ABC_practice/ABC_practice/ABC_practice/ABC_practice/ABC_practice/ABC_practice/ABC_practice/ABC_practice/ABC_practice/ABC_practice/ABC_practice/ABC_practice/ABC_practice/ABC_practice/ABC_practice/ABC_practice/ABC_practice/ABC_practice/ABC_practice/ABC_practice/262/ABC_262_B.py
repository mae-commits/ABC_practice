N, M = map(int,input().split())

U_V = list(list(map(int,input().split())) for i in range(M))

U_V.sort()

count = 0

for i in range(M-2):
    U_V_i = U_V[i]
    for j in range(i+1,M-1):
        U_V_j = U_V[j]
        if U_V_i[0] == U_V_j[0]:
            for k in range(j+1,M):
                U_V_k = U_V[k]
                if U_V_k[0] == U_V_i[1] and U_V_k[1] == U_V_j[1]:
                    count += 1
                    break

print(count)