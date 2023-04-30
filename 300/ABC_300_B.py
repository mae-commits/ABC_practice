H, W = map(int, input().split())

A = list(list(input()) for i in range(H))

B = list(list(input()) for i in range(H))

A_rev = []

for num in range(2):
    for i in range(H):
        A_rev_i = A[i]
        for j in range(W):
            A_rev_i.append(A[i][j])
        A_rev.append(A_rev_i)


print(A_rev)

for i in range(H):
    for j in range(W):
        A_rev_new = [x[j:j+W] for x in A_rev[i:i+H]]
        if A_rev_new == B:
            print('Yes')
            exit()

print('No')