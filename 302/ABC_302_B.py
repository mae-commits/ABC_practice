H, W =  map(int, input().split())

# マス目の入力
S = list(input() for i in range(H))

# 動く方向の組み合わせ
vertical = [0, 1, 1, 1, 0, -1, -1, -1]
horizontal = [1, 1, 0, -1, -1, -1, 0, 1]

for i in range(H):
    for j in range(W):
        for k in range(8):
            if i + 4 * vertical[k] <= H-1 and i + 4 * vertical[k] >= 0 and j + 4 * horizontal[k] <= W-1 and j + 4 * horizontal[k] >= 0:
                ver_k, hor_k = vertical[k], horizontal[k]
                if S[i][j] == 's' and S[i + ver_k][j + hor_k] == 'n' and S[i + 2 * ver_k][j + 2 * hor_k] == 'u' and S[i + 3 * ver_k][j + 3 * hor_k] == 'k' and S[i + 4 * ver_k][j + 4 * hor_k] == 'e':
                    print(i+1, j+1)
                    print(i+ver_k+1, j+hor_k+1)
                    print(i+2*ver_k+1, j+2*hor_k+1)
                    print(i+3*ver_k+1, j+3*hor_k+1)
                    print(i+4*ver_k+1, j+4*hor_k+1) 
                    exit()