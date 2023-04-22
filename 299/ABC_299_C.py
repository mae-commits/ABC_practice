from collections import deque

N = int(input())

S = deque(list(input()))

ans = -1

judge_letters = deque()
last_letter = ''
count_same_continual_letter = 1

for i in range(N): 
    if i == 0:
        last_letter = S.popleft()
    elif i != N-1:
        present_letter = S.popleft()
        if present_letter == last_letter:
            count_same_continual_letter += 1
        else:
            judge_letters.append([last_letter, count_same_continual_letter])
            count_same_continual_letter = 1
            last_letter = present_letter
    else:
        present_letter = S.popleft()
        if present_letter == last_letter:
            count_same_continual_letter += 1
            judge_letters.append([last_letter, count_same_continual_letter])
        else:
            judge_letters.append([last_letter, count_same_continual_letter])
            judge_letters.append([present_letter, 1])
            
length_judge_letters = len(judge_letters)

last_letters = []
present_letters = []

for i in range(length_judge_letters):
    if i == 0:
        last_letters = judge_letters.popleft()
    else:
        present_letters = judge_letters.popleft()
        if last_letters[0] == '-':
            ans = max(ans, present_letters[1])
        else:
            ans = max(ans, last_letters[1])
        last_letters = present_letters

print(ans)