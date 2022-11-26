import sys

h, w = map(int,input().split())

s = []

t = []

for i in range(h):
    s_i = input()
    s.append(s_i)
    
for i in range(h):
    t_i = input()
    t.append(t_i)
        
s_line = {}

t_line = {}

for i in range(w):
    s_line_i = ''
    t_line_i = ''
    for j in range(h):
        s_line_i+=s[j][i]
        t_line_i+=t[j][i]
    if s_line_i not in s_line:
        s_line[s_line_i] = 0
    if t_line_i not in t_line:
        t_line[t_line_i] = 0
    s_line[s_line_i] = s_line[s_line_i] + 1
    t_line[t_line_i] = t_line[t_line_i] + 1

# for name, rows in s_line.items():
#     total = 0
#     for row in rows:
#         total += row[1]
#     s_line[name] = total

# for name, rows in t_line.items():
#     total = 0
#     for row in rows:
#         total += row[1]
#     t_line[name] = total

if s_line == t_line:
    print('Yes')
else:
    print('No')