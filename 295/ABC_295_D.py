# from collections import deque
# import numpy as np

# # 標準入力
# S = deque(list(input()))

# len_S = len(S)

# # 条件を満たす (l,r) の組の個数をカウント
# count = 0

# # 各位の数字の個数をカウント
# digit_number_count = np.array([[0 for i in range(10)]])

# previous_digit_number_count = [0 for i in range(10)]

# # 始めの位を指定し、l桁目までの数字の個数を記録
# for l in range(len_S):
#     lth_num = int(S.popleft())
#     previous_digit_number_count[lth_num]+=1
#     digit_number_count = np.append(digit_number_count, np.array([previous_digit_number_count]), axis=0)

# # 部分文字列の調査
# for l in range(1, len_S+1):
#     # 部分文字列の長さが偶数nである場合のみ
#     # 条件を満足する文字列かどうかを判断
#     for t in range(1,(len_S+1-l)//2 + 1):
#         r = l+2*t-1
#         # l~r文字目までの各数字の文字数を計算
#         dif = digit_number_count[r] - digit_number_count[l-1]
#         if sum(dif%2)==0:
#             count+=1

# print(count)

S = input()

table = [0 for i in range(2**10)]
table[0] = 1
bit = 0

for i in range(len(S)):
    s = int(S[i])
    # これまでの 0 ~ 9 の個数の偶奇を bit で表現
    bit^=2**s
    
    table[bit]+=1

ans = 0

# 各数字について同じ偶奇を持つ組の個数を計上
for t in table:
    ans+=t*(t-1)//2
print(ans)