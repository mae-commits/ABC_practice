"""
from collections import deque

N, M = map(int,input().split())

X = deque(map(int,input().split()))

C_Y = list(list(map(int,input().split())) for i in range(M))

C_Y.sort()

sum = 0

max_point = 0

dp[i][j] is for i th cointoss and j points at the same time.

dp = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(1,N+1):
    X_i = X.popleft()
    for j in range(N+1):
        if j >= 1 and j<= i:
            tmp_max = dp[i-1][j-1] + X_i
            for k in range(len(C_Y)):
                if j == C_Y[k][0]:
                    tmp_max += C_Y[k][1]
                    break
            dp[i][j] = tmp_max
            max_point = max(max_point,tmp_max)
        else:
            dp[i][j] += max_point

print(max_point)
"""

# N: the number of the cointoss.
# M: the number of kinds of continuous bonus.
N,M = map(int,input().split())

# the money you get in i th cointoss if the coin is face.
X = list(map(int,input().split()))

Bonus = [0] * (N+2)

# Input the list "Bonus" into Bonus[C_i] = Y_i
# C_i: the number of counter.
# Y_i: the price of money you can get when the counyter is C_i.
for i in range(M):
    C_i, Y_i = map(int,input().split())
    Bonus[C_i] = Y_i
    
# dp[i][j] means the maximum point when the counter is j and the number of cointoss is i.

dp =[[0 for i in range(N+1)] for j in range(N+1)]

# memorize the maximum number in i th cointoss.
max_point = 0

for i in range(N+1):
    for j in range(i+1):
        if i != 0 and j == 0:
            dp[i][j] = max_point
        elif i != 0 and j != 0:
            dp[i][j] = dp[i-1][j-1] + Bonus[j] + X[i-1]
        max_point = max(max_point,dp[i][j])
    
print(max_point)


