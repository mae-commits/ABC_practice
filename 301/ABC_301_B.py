from collections import deque

N = int(input())

A = deque(list(map(int,input().split())))

new_A = deque()

last_num = A.popleft()
present_num = 0

for i in range(N-1):
    present_num = A.popleft()
    if abs(last_num - present_num) == 1:
        new_A.append(last_num)
        last_num = present_num
    elif last_num > present_num:
        for j in range(last_num, present_num, -1):
            new_A.append(j)
        last_num = present_num
    else:
        for j in range(last_num,present_num):
            new_A.append(j)
        last_num = present_num

new_A.append(present_num)

print(*new_A)