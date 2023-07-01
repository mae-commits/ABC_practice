def dfs(grid, x, y, target, cnt):
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        if cnt == 5:  # 文字列"snuke"の長さが5であることを確認
            return True
        else:
            return False
    
    next_char = "snuke"[cnt % 5]
    if grid[x][y] != target or grid[x][y] != next_char:
        return False
    
    found = False
    temp = grid[x][y]
    grid[x][y] = '.'  # 訪れたマスを一時的に別の文字に置き換える
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '.':
            found |= dfs(grid, nx, ny, next_char, cnt + 1)
    
    grid[x][y] = temp  # 探索終了後にマスを元に戻す
    
    return found

H, W = map(int, input().split())

grid = []
for _ in range(H):
    row = list(input())
    grid.append(row)

found = dfs(grid, 0, 0, 's', 0)

if found:
    print("Yes")
else:
    print("No")
