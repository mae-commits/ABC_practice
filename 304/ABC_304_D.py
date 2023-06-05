from collections import deque, defaultdict

W, H = map(int, input().split())

N = int(input())

def binary_search(s, a, b, A, B):
    s_x, s_y = s[0], s[1]
    left_a, right_a = 0, A - 1
    left_b, right_b = 0, B - 1

    while left_a <= right_a:
        mid_a = (left_a + right_a) // 2
        if a[mid_a] == s_x:
            break
        elif a[mid_a] < s_x:
            left_a = mid_a + 1
        else:
            right_a = mid_a - 1
    else:
        mid_a = right_a

    while left_b <= right_b:
        mid_b = (left_b + right_b) // 2
        if b[mid_b] == s_y:
            break
        elif b[mid_b] < s_y:
            left_b = mid_b + 1
        else:
            right_b = mid_b - 1
    else:
        mid_b = right_b

    region = str(mid_a) + str(mid_b)
    return region
            
strawberries = deque([])

for i in range(N):
    strawberries.append(list(map(int, input().split())))

A = int(input()) + 2

a = [0] + list(map(int, input().split())) + [W]

B = int(input()) + 2

b = [0] + list(map(int, input().split())) + [H]

group = defaultdict(int)

for i in range(N):
    strawberry = strawberries.popleft()
    # 2分探索でどの領域にあるかを確認
    region = binary_search(strawberry, a, b, A, B)
    group[region] += 1

if N >= (A-1) * (B-1) and len(group) >= N:
    print(min(group.values()), max(group.values()))
else:
    print(0, max(group.values()))