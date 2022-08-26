R, C = map(int,input().split())

grid = [[0 for i in range(16)] for j in range(16)]

for i in range(1,16):
    for j in range(1,16):
        if i == 1 or i == 15:
            grid[i][j] = "black"
        elif j == 1 or j == 15:
            grid[i][j] = "black"
        elif (i == 3 or i == 13) and (j >= 3 and j <= 13):
            grid[i][j] = "black"
        elif (i == 5 or i == 11) and (j >= 5 and j <= 11):
            grid[i][j] = "black"
        elif (i == 7 or i == 9) and (j >= 7 and j <= 9):
            grid[i][j] = "black"
        elif (i == 4 or i == 12) and (j == 3 or j == 13):
            grid[i][j] = "black"
        elif (i == 6 or i == 10) and (j == 3 or j == 13 or j == 5 or j == 11):
            grid[i][j] = "black"
        elif i == 8 and (j == 3 or j == 13 or j == 5 or j == 11 or j == 7 or j == 9):
            grid[i][j] = "black"
        else:
            grid[i][j] = "white"

print(grid[R][C])