def solve(N, data):
    diff = []  # 青木派から高橋派への人数差のリスト
    for X, Y, _ in data:
        diff.append(X - Y)
    
    diff.sort(reverse=True)  # 人数差を降順にソート
    
    total_seats = sum(data[i][2] for i in range(N))
    needed_seats = (total_seats + 1) // 2  # 過半数の議席数
    
    ans = 0
    curr_sum = 0  # 選挙区を順に見ていき、人数差が正になるまでの人数差の合計
    idx = 0
    while idx < N and curr_sum + diff[idx] < needed_seats:
        curr_sum += diff[idx]
        idx += 1
        ans += 1
    
    return ans

# 入力を受け取る
N = int(input())
data = []
for _ in range(N):
    X, Y, Z = map(int, input().split())
    data.append((X, Y, Z))

result = solve(N, data)
print(result)
