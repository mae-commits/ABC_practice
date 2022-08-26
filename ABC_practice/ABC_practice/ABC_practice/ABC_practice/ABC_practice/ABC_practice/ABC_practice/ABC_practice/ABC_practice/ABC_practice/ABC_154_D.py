"""
N, K = map(int,input().split())

p = [0] + list(map(int,input().split()))

expect_value = [0 for i in range(N+1)]

for i in range(1,N+1):
    expect_value[i] = (1+p[i])/2

# print(expect_value)

accumulation_sum = [0 for i in range(N+1)]

for i in range(1,N+1):
    accumulation_sum[i] = accumulation_sum[i-1] + expect_value[i]

# print(accumulation_sum)
max_sum = -10**15 

partial_sum = 0

for i in range(1,N-K+1):
    partial_sum = accumulation_sum[i+K-1] - accumulation_sum[i-1]
    max_sum = max(partial_sum, max_sum)
    
print(max_sum)    
"""

N, K = map(int,input().split())

p = [0] + list(map(int,input().split()))

expect_value = [0 for i in range(N+1)]

for i in range(1,N+1):
    expect_value[i] = (1+p[i])/2

# print(expect_value)

accumulation_sum = [0 for i in range(N+1)]

for i in range(1,N+1):
    accumulation_sum[i] = accumulation_sum[i-1] + expect_value[i]

# print(accumulation_sum)
max_sum = -10**15 

partial_sum = 0

for i in range(1,N-K+1):
    partial_sum = accumulation_sum[i+K-1] - accumulation_sum[i-1]
    max_sum = max(partial_sum, max_sum)
    
print(max_sum)