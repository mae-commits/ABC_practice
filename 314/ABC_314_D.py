from collections import deque

N = int(input())

S = list(input())

sign = [0]

Q = int(input())

# 小文字(-)・大文字(+)の変化を符号で表す（変化しない時は0）。

change = []
change_max = 0

for i in range(Q):
    t, x, c = map(str, input().split())
    if t == '1':    
        change.append([i+1, int(x)-1, c])
        sign.append(0)
    elif t == '2':
        sign.append(-1)
        change_max = i+1
    else:
        sign.append(1)
        change_max = i+1

change_length = len(change)
change = deque(change)

if change_max == 0:
    for i in range(change_length):
        change_i = change.popleft()
        S[change_i[1]] = change_i[2]
    print(S)
else:
    change_i = change.popleft()
    max_sign = sign[change_max]
    num = 1
    while change_i[0] <= change_max and num <= Q:
        S[change_i[1]] = change_i[2]
        num += 1
    S = "".join(S)
    if max_sign == 1:
        S.upper()
    else:
        S.lower()
    while len(change) >= 1 and num <= Q:
        change_i = change.popleft()
        S[change_i[1]] = change_i[2]
        num += 1
    S = "".join(S)
    print(S)
                    
#     if t == '1':
#         S[int(x)-1] = c
#         sign[int(x)-1] = 0
#     elif t == '2':
#         sign = sign_lower
#     else:
#         sign = sign_upper

# sign = deque(sign)        
# ans = ''
# S = deque(S)

# for i in range(N):
#     sign_i = sign.popleft()
#     S_i = S.popleft()
#     if sign_i == 0:
#         ans += S_i
#     elif sign_i == -1:
#         ans += S_i.lower()
#     else:
#         ans += S_i.upper()

# print(ans)