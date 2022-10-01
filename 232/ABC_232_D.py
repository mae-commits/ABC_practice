h, w = map(int,input().split())

c = ['#'] + list(('#' + input()) for i in range(h))

dist = [[-1]*(w+1) for i in range(h+1)]

dist[1][1] = 1

ans = -1

for i in range(1,h+1):
    for j in range(1,w+1):
        if i == 1 and j != 1:
            if (c[i][j-1] != '#' and dist[i][j-1] != -1) and c[i][j] != '#':
                dist[i][j] = dist[i][j-1] + 1
        elif i != 1 and j == 1:
            if (c[i-1][j] != '#' and dist[i-1][j] != -1) and c[i][j] != '#':
                dist[i][j] = dist[i-1][j] + 1
        elif i != 1 and j != 1:
            if ((c[i-1][j] != '#' and dist[i-1][j] != -1) or (c[i][j-1] != '#' and dist[i][j-1] != -1)) and c[i][j] != '#':
                dist[i][j] = max(dist[i-1][j], dist[i][j-1]) + 1
        ans = max(dist[i][j],ans)
        
print(ans)
