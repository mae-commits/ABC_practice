from collections import deque
import sys
s = deque(list(input()))
t = deque(list(input()))

len_s = len(s)

for i in range(len_s):
    s_i = s.popleft()
    t_i = t.popleft()
    if s_i != t_i:
        print(i+1)
        sys.exit()
print(len_s + 1)
