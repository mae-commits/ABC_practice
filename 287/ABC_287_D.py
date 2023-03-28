from collections import deque

s = list(input())
t = list(input())

t_length = len(t)

head = [False]*(len(s)+1)

head[0] = True

# 先頭 i 文字の判定
for i in range(t_length):
    if not (s[i] == t[i] or t[i] == "?" or s[i] == "?"):
        break
    head[i+1] = True

tail = [False]*(len(s)+1)

tail[0] = True

s.reverse()
t.reverse()

# 末尾 i 文字の判定

for i in range(t_length):
    if not (s[i] == t[i] or t[i] == "?" or s[i] == "?"):
        break
    tail[i+1] = True

for i in range(t_length+1):
    if head[i] & tail[t_length - i] == True:
        print("Yes")
    else:
        print("No")