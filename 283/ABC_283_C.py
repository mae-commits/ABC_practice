from collections import deque

s = deque(list(input()))

s_len = len(s)

count = 0

last_num = 'a'
zero_continue = 0

for i in range(s_len):
    s_ith = s.pop()
    if s_ith == '0' and last_num == '0' and zero_continue == 1:
        zero_continue = 0
        last_num = 'a'
    elif s_ith == '0':
        zero_continue = 1
        last_num = '0'
        count+=1
    else:
        zero_continue = 0
        last_num = s_ith
        count+=1

print(count)