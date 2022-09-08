from collections import deque

def solve():
    s = input()
    k = int(input())
    que = deque()
    rem = k
    ans, score = 0, 0
    for char in s:
        score += 1
        if char == '.':
            que.append(1)
            rem -= 1
        else:
            que.append(0)
        
        while rem < 0:
            rem += que.popleft()
            score -= 1
        
        ans = max(ans, score)
    
    return ans

print(solve())
            

# s = '.' + input()
# k = int(input())
# # dp[i][j]: i: the number of continuous 'X' for ith order in string 's',
# # j: and the number of 'X' you change from '.' to 'X'
# dp = [[0 for j in range(k+1)] for i in range(len(s))]

# dp[1][0] = s[1].count('X')

# if len(s) >= 3:
#     for i in range(2,len(s)):
#         dp[i][0] = dp[i-1][0] + s[i].count('X')

# for j in range(1,k+1):
#     dp[0][j] = -1

# continious = []

# if len(s) >= 3:
#     for i in range(2,len(s)):
#         for j in range(1,k+1):
#             if j>i-dp[i][0]:
#                 dp[i][j] = -1
#             elif s[i] == 'X':
#                 dp[i][j] = dp[i-1][j] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j])

# print(max(dp[len(s)-1]))