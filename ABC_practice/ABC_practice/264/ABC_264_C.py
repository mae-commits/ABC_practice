import sys

H_1, W_1 = map(int,input().split())

A = list(list(map(int,input().split())) for i in range(H_1))
    
H_2, W_2 = map(int,input().split())

B = list(list(map(int,input().split())) for i in range(H_2))

B_flatten = []

for i in range(H_2):
    for j in range(W_2):
        B_flatten.append(B[i][j])

len_B = len(B_flatten)

# print(B_flatten)

if H_1 < H_2 or W_1 < W_2:
    print("No")
    sys.exit()
    
# bit all search for lines.
# 1: not extracted(use for A_new), 0: extracted(not use for A_new) 
else:
    for H_i in range(1 << H_1):
        for W_i in range(1 << W_1):
            count = 0
            A_flatten = []
            # count_True = True
            for H_j in range(H_1):
                for W_j in range(W_1):
                    if H_i >> H_j & 1 == 1 and W_i >> W_j & 1 == 1:
                        A_flatten.append(A[H_j][W_j])
                        count += 1
            if count == len_B:
                # print(A_flatten)
                if A_flatten == B_flatten:
                    print("Yes")
                    sys.exit()
                    
print("No")