S = list(map(int, input().split()))

for i in range(len(S)):
    if i != 0:
        if S[i] >= S[i-1] and S[i] >= 100 and S[i] <=675 and S[i] % 25  == 0:
            continue
        else:
            print("No")
            exit()
    elif S[i] >= 100 and S[i] <=675 and S[i] % 25  == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")