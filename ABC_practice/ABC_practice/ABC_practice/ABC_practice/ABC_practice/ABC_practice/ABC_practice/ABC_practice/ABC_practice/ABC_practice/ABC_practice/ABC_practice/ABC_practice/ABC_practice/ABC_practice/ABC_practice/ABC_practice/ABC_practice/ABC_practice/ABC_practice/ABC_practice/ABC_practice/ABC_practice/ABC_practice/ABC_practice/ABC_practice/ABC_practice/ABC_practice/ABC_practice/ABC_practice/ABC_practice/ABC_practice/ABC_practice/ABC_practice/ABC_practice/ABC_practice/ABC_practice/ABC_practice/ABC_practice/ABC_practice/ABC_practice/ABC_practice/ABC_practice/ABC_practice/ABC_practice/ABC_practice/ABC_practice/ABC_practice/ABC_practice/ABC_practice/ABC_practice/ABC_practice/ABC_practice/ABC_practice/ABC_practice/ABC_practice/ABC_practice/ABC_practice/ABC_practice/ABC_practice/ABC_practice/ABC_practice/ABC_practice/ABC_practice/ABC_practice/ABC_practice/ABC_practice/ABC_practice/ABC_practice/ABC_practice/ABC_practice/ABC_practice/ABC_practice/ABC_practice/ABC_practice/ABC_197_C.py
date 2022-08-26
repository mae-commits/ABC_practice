N = int(input())

A = list(map(int,input().split()))

# Define the answer.
ans = 10 ** 10

for i in range(1 << (N-1)):
    # Resister the recent number of divisor place.
    recent_num = 1
    ans_tmp = 0
    for j in range(N-1):
        if i >> j & 1 == 1:
            ans_tmp_group = 0
            for k in range(recent_num+1, j+1):
                # calculate the temporary binary value by "OR" in the same group.
                ans_tmp_group = ans_tmp_group | A[k]
            ans_tmp = ans_tmp ^ ans_tmp_group
            recent_num = j
    ans = min(ans,ans_tmp)

print(ans)            