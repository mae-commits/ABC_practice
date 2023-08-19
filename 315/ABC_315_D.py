def solve(H, W, cookies):
    marked_rows = [False] * H
    marked_cols = [False] * W
    
    for i in range(H):
        for j in range(W):
            if cookies[i][j] == '.':
                continue
            
            row_count = cookies[i].count(cookies[i][j])
            col_count = sum(1 for k in range(H) if cookies[k][j] == cookies[i][j])
            
            if row_count >= 2:
                marked_rows[i] = True
            if col_count >= 2:
                marked_cols[j] = True
    
    new_cookies = []
    for i in range(H):
        if not marked_rows[i]:
            new_row = [cookies[i][j] for j in range(W) if not marked_cols[j]]
            new_cookies.append(new_row)
    
    remaining_cookies = sum(row.count('.') for row in new_cookies)
    return remaining_cookies

H, W = map(int, input().split())
cookies = [input().strip() for _ in range(H)]
result = solve(H, W, cookies)
print(result)
