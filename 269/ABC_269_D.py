N = int(input())

XY = list(list(map(int,input().split())) for i in range(N))

grid = [[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1]]

ans = 0

