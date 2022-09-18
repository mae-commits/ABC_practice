import sys 

N = int(input())

N_bin = str(bin(N)[2:])

len_N_bin = len(N_bin)

one_digits = []

if N == 0:
    print(0)
    sys.exit()

for i in range(len_N_bin):
    if N_bin[i] == '1':
        one_digits.append(len_N_bin - i)

one_digits = sorted(one_digits)

ans = []
        
for i in range(1 << len(one_digits)):
    tmp_ans = 0
    for j in range(len(one_digits)):
        if i >> j & 1 == True:
            tmp_ans += 2 ** (one_digits[j]-1)
    ans.append(tmp_ans)
    
for i in ans:
    print(i)            