from collections import deque

X, Y, Z = map(int, input().split())

S = deque(list(input()))

# 文字列Sの文字数
length =len(S)

# dp[i][0], dp[i][1]: CapsLockが OFF, ON 状態
dp = [[0]*2 for _ in range(length+1)]

# OFF -> OFF, OFF -> ON, ON -> ON, ON -> OFF で a, A を打つ時間
time = [[X, Y], [Z+Y, Z+X], [Y, X], [Z+X, Z+Y]]
for i in range(1, length+1):
    S_i = S.popleft()
    # 次の文字を打つためにかかる時間
    # a
    if S_i == 'a':
        time_consumed = [time[0][0], time[1][0], time[2][0], time[3][0]]
    # A
    else:
        time_consumed = [time[0][1], time[1][1], time[2][1], time[3][1]]
    if i != 1:
        dp[i][0] = min(dp[i-1][0]+time_consumed[0], dp[i-1][1]+time_consumed[3])
        dp[i][1] = min(dp[i-1][0]+time_consumed[1], dp[i-1][1]+time_consumed[2])
    else:
        dp[i][0] = dp[i-1][0]+time_consumed[0]
        dp[i][1] = dp[i-1][0]+time_consumed[1]

print(min(dp[-1]))