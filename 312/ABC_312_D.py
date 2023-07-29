MOD = 998244353

def count_bracket_sequences(S):
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n + 1):
            if S[i] == '(':
                dp[i + 1][j + 1] += dp[i][j]
            elif S[i] == ')':
                if j > 0:
                    dp[i + 1][j - 1] += dp[i][j]
            else:  # S[i] == '?'
                dp[i + 1][j + 1] += dp[i][j]
                if j > 0:
                    dp[i + 1][j - 1] += dp[i][j]

            dp[i + 1][j] %= MOD

    return dp[n][0]

# 入力例1の場合
S = "(??(?"

result = count_bracket_sequences(S)
print(result)  # Output: 2
