N, M = map(int, input().split())

S = list(input() for i in range(N))

ref_bl = '###.###.###.....'
ref_br = '.....###.###.###'

# 左上のマス目を最初に決定し、全探索
for i in range(N-8):
    for j in range(M-8):
        left_upper = S[i][j:j+4] + S[i+1][j:j+4] + S[i+2][j:j+4] + S[i+3][j:j+4]
        right_below = S[i+5][j+5:j+9] + S[i+6][j+5:j+9] + S[i+7][j+5:j+9] + S[i+8][j+5:j+9]
        if left_upper == ref_bl and right_below == ref_br:
            print(i+1, j+1)