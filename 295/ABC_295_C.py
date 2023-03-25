from collections import deque

N = int(input())

A = sorted(list(map(int,input().split())))

A = deque(A)
count = 0

ex_color = ""

for i in range(N):
    present_color = A.popleft()
    # 色が一緒ならば、ペアを作る（前の色が残っている場合）
    if ex_color == present_color:
        count += 1
        ex_color = ""
    else:
        ex_color = present_color

print(count)