import sys

S = input()
last_num = -1
for i in range(len(S)):
    if S[i] == 'a':
        last_num = i+1

print(last_num)