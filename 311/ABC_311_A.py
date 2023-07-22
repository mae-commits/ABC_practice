N = int(input())

S = input()

ans = 0

count_ABC = [0, 0, 0]

for i in range(N):
    ans += 1
    if S[i] == 'A':
        count_ABC[0] += 1
    elif S[i] == 'B':
        count_ABC[1] += 1
    else:
        count_ABC[2] += 1
    if count_ABC[0] >= 1 and count_ABC[1] >= 1  and count_ABC[2] >= 1:
        print(ans)
        exit()