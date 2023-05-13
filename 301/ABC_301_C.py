from collections import deque
import numpy as np

S = deque(list(input()))

T = deque(list(input()))

card_num = len(S)

S_letter = np.array([0 for i in range(26)])
T_letter = np.array([0 for i in range(26)])

S_at = 0
T_at = 0

for i in range(card_num):
    s_letter = S.popleft()
    t_letter = T.popleft()
    if s_letter == "@":
        S_at += 1
    else:
        S_letter[ord(s_letter)-97] += 1    
    if t_letter == "@":
        T_at += 1
    else:
        T_letter[ord(t_letter)-97] += 1

dif = abs(S_letter - T_letter)
dif_rev = S_letter - T_letter
atcoder = [dif_rev[0], dif_rev[2], dif_rev[3], dif_rev[4], dif_rev[14], dif_rev[17], dif_rev[19]]
S_change = 0
T_change = 0

for i in range(26):
    # 1 5 6 7 8 9 10 11 12 13 15 16 18 20 21 22 23 24 25
    # b f g h i j k  l  m  n  p  q  s  u  v  w  x  y  z
    if (dif[1] + dif[5] + dif[6] + dif[7] + dif[8] + dif[9] + dif[10] + dif[11] + dif[12] + dif[13] + dif[15] + dif[16] + dif[18] + dif[20] + dif[21] + dif[22] + dif[23] + dif[24] + dif[25]) != 0:
        print("No")
        exit()

for i in range(len(atcoder)):
    if atcoder[i] > 0:
        T_change += abs(atcoder[i])
    elif atcoder[i] < 0:
        S_change += abs(atcoder[i])

if T_change > T_at or S_change > S_at:
    print("No")
else:
    print("Yes")