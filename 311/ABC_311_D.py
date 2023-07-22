def dfs(grid, i, j, visited):
    if i < 1 or i > len(grid) - 2 or j < 1 or j > len(grid[0]) - 2 or grid[i][j] == '#':
        return 0

    if (i, j) in visited:
        return 0

    visited.add((i, j))

    ice_count = 0

    if grid[i][j] == '.':
        # 同じ方向に進み続ける
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            ice_count += dfs(grid, i + dx, j + dy, visited)
    else:
        # 氷の上を通る場合は方向転換せずに進む
        ice_count += dfs(grid, i, j, visited)

    return ice_count + 1  # 現在のマスをカウントする

def main():
    N, M = map(int, input().split())
    grid = [['#'] * (M + 2)]  # 周囲を岩で囲む
    for _ in range(N):
        grid.append(['#'] + list(input()) + ['#'])
    grid.append(['#'] * (M + 2))  # 周囲を岩で囲む

    visited = set()  # 訪れたマスを記録するためのセット
    result = dfs(grid, 2, 2, visited)  # 最初は右方向に進む
    print(result)

if __name__ == "__main__":
    main()
