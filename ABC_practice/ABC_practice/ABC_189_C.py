N = int(input())

A = list(map(int,input().split()))

x = 0

max_sum = 0

sum_tmp = 0

for i in range(N):
    x = A[i]
    for j in range(i,N):
        x = min(x,A[j])
        sum_tmp = x * (j-i+1)
        max_sum = max(sum_tmp, max_sum)        

print(max_sum)
