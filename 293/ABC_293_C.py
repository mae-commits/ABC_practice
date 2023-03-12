import itertools

h, w = map(int,input().split())

a = list(list(map(int,input().split())) for i in range(h))

count = 0

# bit 全探索により全ての場合を考える
# 0: 縦方向の移動
# 1: 横方向の移動
# 縦、横方向の移動がマス内に収まるように管理
for bit in range(1 << (h+w-2)):
    vertical,horizontal = 0, 0
    route = set([a[0][0]])
    for j in range(h+w-2):
        if (bit & (1 << j)):
            if horizontal < w-1:
                horizontal+=1
                route.add(a[vertical][horizontal])  
        else:
            if vertical < h-1:
                vertical+=1
                route.add(a[vertical][horizontal])         
        # print(vertical,horizontal)
        # print(route)
    if len(route) == h+w-1:
        count+=1

print(count)
        
# for v in p:
#     vertical = 0
#     horizontal = 0
#     route = set([first_state])
#     for verify in v:
#         if verify == True:
#             # print(a[vertical+1][horizontal])
#             vertical+=1
#             route.add(a[vertical][horizontal])
#         else:
#             # print(a[vertical][horizontal+1])
#             horizontal+=1
#             route.add(a[vertical][horizontal])
#         # print(vertical, horizontal)
#     # print("done")
#     if len(route) == h+w-1:
#         count+=1