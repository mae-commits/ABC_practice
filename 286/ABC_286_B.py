from collections import deque

n = int(input())

s_list = list(input())

s = deque(s_list)

s_new = ""

s_last = ""

for i in range(n):
    s_now = s.popleft()
    if s_last == "n" and s_now == "a":
        s_new+="nya"
        s_last = ""
    elif s_now != "a":
        s_new+=s_last
        s_last=s_now
    elif s_now != "n":
        s_new+=s_last
        s_last=s_now
    if i == n-1:
        s_new+=s_last

print(s_new)