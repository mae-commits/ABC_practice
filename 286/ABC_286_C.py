from collections import deque

n,a,b=map(int,input().split())

s = deque(list(input()))


count = [a*i for i in range(n)]

s_new_list = [list(s)]

for i in range(n):
    s_new = s.popleft()
    s.append(s_new)
    s_new_list.append(list(s))

s_new_list = deque(s_new_list)

for i in range(n):
    s_list = s_new_list.popleft()
    count_i = count[i]
    for j in range(n//2):
        if s_list[j] != s_list[n-1-j]:
            count_i+=b
    count[i]=count_i

print(min(count))