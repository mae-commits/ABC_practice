from collections import deque

n = int(input())

s = deque(list(input()))

s_new = ''
even_odd = False

for i in range(n):
    s_i = s.popleft()
    if s_i == '"':
        even_odd = not even_odd
    elif even_odd == False and s_i == ',':
        s_i = '.'
    s_new+=s_i

print(s_new)
    