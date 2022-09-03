from collections import deque
N, M = map(int,input().split())

A = list(map(int,input().split()))

A_last = deque(A[M:N])

partialSum = deque([])

A_deq = deque(A)

initialSum = sum(A[0:M])

partialSum.append(initialSum)

for i in range(1,N-M+1):
    initialSum = initialSum+A[i+M-1]-A[i-1]
    partialSum.append(initialSum)
    
sum = 0
for i in range(M):
    A_i = A_deq.popleft()
    sum += A_i * (i+1) # Initial sum

maxSum = sum

for i in range(1,N-M+1):
    parSum = partialSum.popleft()
    appendA = A_last.popleft()
    sum = sum - parSum + appendA * M
    maxSum = max(sum,maxSum)

print(maxSum)    