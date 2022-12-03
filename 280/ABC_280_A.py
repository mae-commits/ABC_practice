h, w = map(int,input().split())

s = list(input() for i in range(h))

count = 0

for i in range(h):
    s_i = s[i]
    for j in range(w):
        if s_i[j] == '#':
            count+=1
print(count)