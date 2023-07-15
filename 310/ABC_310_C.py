N = int(input())

S = list(input() for i in range(N))

S = set(S)

ans = len(S)

S_list = list(S)

for i in range(len(S_list)):
    num = S_list[i]
    num_reverse = num[::-1]
    if num_reverse in S and num != num_reverse:
        ans -= 1
        S.remove(num)
        
print(ans)
