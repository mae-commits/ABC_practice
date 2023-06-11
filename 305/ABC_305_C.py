H, W = map(int, input().split())

S = [['.' for i in range(W+2)]]
for i in range(H):
    S_line = ['.'] + list(input()) + ['.']
    S.append(S_line)
S.append(['.' for i in range(W+2)])
grid_x = [-1, 0, 1, 0]
grid_y = [0, -1, 0, 1]

for i in range(1, H+1):
    for j in range(1, W+1):
        count_cookies = 0
        for k in range(4):
            x = i + grid_x[k]
            y = j + grid_y[k]
            if S[x][y] == '#' and S[i][j] == '.':
                count_cookies += 1
            if count_cookies >= 2:
                print(i, j)
                exit()