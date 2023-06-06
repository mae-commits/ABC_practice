from collections import deque, defaultdict
from bisect import bisect_left

W, H = map(int, input().split())

N = int(input())

# 二分探索
def binary_search(s, a, b, A, B):
    s_x, s_y = s[0], s[1]
    left_a, right_a = 0, A
    left_b, right_b = 0, B

    while left_a < right_a:
        mid_a = (left_a + right_a) // 2
        if a[mid_a] < s_x:
            left_a = mid_a + 1
        else:
            right_a = mid_a

    while left_b < right_b:
        mid_b = (left_b + right_b) // 2
        if b[mid_b] < s_y:
            left_b = mid_b + 1
        else:
            right_b = mid_b

    region = (left_a, left_b)
    return region
            
strawberries = deque()

for i in range(N):
    strawberries.append(list(map(int, input().split())))

A = int(input())

a = list(map(int, input().split()))

B = int(input())

b = list(map(int, input().split()))

# 各領域に存在するいちごの数をカウント
group = defaultdict(int)

for i in range(N):
    strawberry = strawberries.popleft()
    # 2分探索でどの領域にあるかを確認
    region = binary_search(strawberry, a, b, A, B)
    group[region] += 1

if len(group) >= (A+1) * (B+1):
    print(min(group.values()), max(group.values()))
else:
    print(0, max(group.values()))