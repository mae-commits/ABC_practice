from collections import defaultdict

N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))

A_dic = defaultdict(int)

ans_tmp_initial = 0

for i in A:
    A_dic[i] += 1
    ans_tmp_initial += i
    
# for key, value in zip(A_dic.keys(), A_dic.values()):
#     ans_tmp_initial +=  key * value

initial = 0

# 最初のインデックスを決定
initial_num = A[0]
while True:
    if not initial_num in A_dic.keys():
        initial_num = (initial_num-1)%M
        break
    else:
        initial_num = (initial_num + 1) % M

ans = -1
ans_tmp = ans_tmp_initial

for i in A_dic.keys():
    if (initial_num%M) in A_dic.keys():
        ans_tmp -= (i%M) * A_dic[i%M]
        ans = min(ans_tmp, ans) if not ans == -1 else ans_tmp
    else:
        ans_tmp = ans_tmp_initial

print(ans)