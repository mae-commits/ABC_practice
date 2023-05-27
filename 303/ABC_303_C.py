# from collections import deque

N, M, H, K = map(int, input().split())

# S = deque(list(input()))

# # 高橋くんの位置
# place = [0, 0]

# # 高橋くんの体力
# hit_point = H

# coordinates = []

# for i in range(M):
#     new_point = list(map(int, input().split()))
#     coordinates.append(new_point)

# move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# for i in range(N):
#     S_i = S.popleft()
#     if S_i == 'R':
#         place[0] += move[0][0]
#         place[1] += move[0][1]
#     elif S_i == 'L':
#         place[0] += move[1][0]
#         place[1] += move[1][1]
#     elif S_i == 'U':
#         place[0] += move[2][0]
#         place[1] += move[2][1]
#     else:
#         place[0] += move[3][0]
#         place[1] += move[3][1]
#     hit_point -= 1
#     if hit_point < 0:
#         print('No')
#         exit()
#     if hit_point < K:
#         if place in coordinates:
#             hit_point = K
#     # print(hit_point)
# print('Yes')
def can_complete_moves(N, M, H, K, S, items):
    x, y = 0, 0  # 高橋くんの座標
    item_positions = set(items)  # アイテムの座標を集合として管理
    
    for i in range(N):
        # 移動先の座標を計算
        if S[i] == 'R':
            x += 1
        elif S[i] == 'L':
            x -= 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
        
        H -= 1  # 体力を消費
        
        if H < 0:
            return False  # 体力が負になった場合、移動を中止
        
        # 移動先にアイテムがあり、かつ体力がK未満の場合
        if (x, y) in item_positions and H < K:
            item_positions.remove((x, y))  # アイテムを使用
            H = K  # 体力をKに回復
    
    return True

# 入力例
S = input()
items = [tuple(map(int, input().split())) for _ in range(M)]

result = can_complete_moves(N, M, H, K, S, items)
if result:
    print("Yes")
else:
    print("No")
