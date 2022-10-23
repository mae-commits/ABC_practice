h, w = map(int,input().split())

c = list(list(input()) for i in range(h))

x = [0 for i in range(w+1)]

for i in range(h):
    for j in range(w):
        if c[i][j] == '#':
            x[j+1] += 1
            
print(*x[1:])