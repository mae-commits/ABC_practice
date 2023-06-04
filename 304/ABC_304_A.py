N =  int(input())

S = []
A = []
youngest = 10 ** 9 + 1
youngest_index = -1

for i in range(N):
    S_i, A_i = map(str, input().split())
    A_i = int(A_i)
    S.append(S_i)
    A.append(A_i)
    youngest = min(youngest, A_i)
    if youngest == A_i:
        youngest_index = i

ans = S[youngest_index:N] + S[0:youngest_index] if youngest_index != 0 else S

for i in ans:
    print(i)