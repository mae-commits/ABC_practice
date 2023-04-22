from collections import deque

N, T = map(int, input().split())

colors = deque(list(map(int, input().split())))
numbers = deque(list(map(int, input().split())))

max_number = 0

winner = 0

max_alternative_number = 0

alternative_winner = 0

alternative_color = 0

for i in range(N):
    ith_color = colors.popleft()
    ith_number = numbers.popleft()
    if ith_color == T and max(max_number, ith_number) == ith_number:
        winner = i+1
        max_number = ith_number
    if i == 0:
        max_alternative_number = ith_number
        alternative_winner = 1
        alternative_color = ith_color
    if ith_color == alternative_color and max(max_alternative_number, ith_number) == ith_number:
        max_alternative_number = ith_number
        alternative_winner = i+1

if winner != 0:
    print(winner)
    exit()
else:
    print(alternative_winner)
    exit()