from collections import deque

n = int(input())

diviser = 998244353

dp = [[0,0]for i in range(n+1)]

numbers = deque(list(map(int,input().split())) for i in range(n))

first_numbers = numbers.popleft()

last_numbers = [first_numbers[0],first_numbers[1]]

# Initial number of cases 
dp[1] = [1,1]

for i in range(1,n):
    new_numbers = numbers.popleft()
    if last_numbers[0] != new_numbers[0] and last_numbers[1] != new_numbers[0]:
        dp[i+1][0] = (dp[i][0] + dp[i][1])%diviser
    elif last_numbers[0] != new_numbers[0]:
        dp[i+1][0] = dp[i][0]
    elif last_numbers[1] != new_numbers[0]:
        dp[i+1][0] = dp[i][1]
    if last_numbers[0] != new_numbers[1] and last_numbers[1] != new_numbers[1]:
        dp[i+1][1] = (dp[i][0] + dp[i][1])%diviser
    elif last_numbers[0] != new_numbers[1]:
        dp[i+1][1] = dp[i][0]
    elif last_numbers[1] != new_numbers[1]:
        dp[i+1][1] = dp[i][1]
    last_numbers = new_numbers

print(sum(dp[n])%diviser)