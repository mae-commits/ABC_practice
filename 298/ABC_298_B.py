N = int(input())

A = list(list(map(int, input().split())) for i in range(N))

B = list(list(map(int, input().split())) for i in range(N))

A_1_tile_count = []

# Aの配列中に1がどのインデックスに存在するかを判定

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            A_1_tile_count.append([i, j])


if len(A_1_tile_count) == 0:
    print("Yes")
    exit()
# 回転回数

for i in range(4):
    # 条件を満たしているタイルの個数
    count_same = 0
    # 回転後のAの配列のインデックスがBのそれに一致しているかどうかを確認
    for j in range(len(A_1_tile_count)):
        x, y = A_1_tile_count[j][0], A_1_tile_count[j][1]
        if B[x][y] == 1:
            count_same += 1
        # 条件を満たしている場合は終了
        if count_same == len(A_1_tile_count) and j == len(A_1_tile_count) - 1:
            print("Yes")
            exit()
        # 調査が終わった座標は回転
        A_1_tile_count[j] = [N-1-y, x]
print("No")