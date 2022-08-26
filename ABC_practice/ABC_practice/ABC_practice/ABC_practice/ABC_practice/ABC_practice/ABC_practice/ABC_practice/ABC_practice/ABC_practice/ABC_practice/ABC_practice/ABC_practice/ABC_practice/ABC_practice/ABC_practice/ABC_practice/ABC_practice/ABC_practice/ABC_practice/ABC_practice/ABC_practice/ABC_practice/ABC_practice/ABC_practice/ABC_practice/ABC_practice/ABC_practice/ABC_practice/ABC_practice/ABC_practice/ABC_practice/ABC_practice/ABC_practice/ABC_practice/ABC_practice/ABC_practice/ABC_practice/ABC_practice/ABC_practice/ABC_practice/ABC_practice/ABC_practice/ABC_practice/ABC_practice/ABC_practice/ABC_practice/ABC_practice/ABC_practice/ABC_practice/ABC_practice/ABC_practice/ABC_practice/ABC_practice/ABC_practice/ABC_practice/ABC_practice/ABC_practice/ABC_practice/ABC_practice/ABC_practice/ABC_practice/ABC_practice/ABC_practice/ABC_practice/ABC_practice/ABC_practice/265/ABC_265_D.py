import sys

N, P, Q, R = map(int,input().split())

A = list(map(int,input().split()))

total_sum = [0 for i in range(N)]
total_sum[0] = A[0]

for i in range(1, N):
    total_sum[i] = total_sum[i-1] + A[i]
    
"""
for x in range(N-3):
    for y in range(x+1, N-2):
        total_sum_1 = total_sum[y-1] - total_sum[x-1]
        if total_sum_1 != P:
            continue
        for z in range(y+1, N-1):
            total_sum_2 = total_sum[z-1] - total_sum[y-1]
            if total_sum_2 != Q:
                continue
            for w in range(z+1, N):
                total_sum_3 = total_sum[w-1] - total_sum[z-1]
                if total_sum_3 == R:
                    print("Yes")
                    sys.exit()
"""
y = N-3
z = N-2
w = N-1

for x in range(N-3):
    sum_1 = 0
    while sum_1 != P and y > x:
        sum_1 = total_sum[y-1] - total_sum[x-1]
        if sum_1 > P:
            y = (x+y)//2
        elif sum_1 < P:
            y = (y+N-3)//2
    if sum_1 != P:
        continue
    sum_2 = 0
    while sum_2 != Q and z > y:
        sum_1 = total_sum[z-1] - total_sum[y-1]
        if sum_2 > Q:
            z = (y+z)//2
        elif sum_2 < Q:
            z = (z+N-2)//2
    if sum_2 != Q:
        continue
    sum_3 = 0
    while sum_3 != R and w > z:
        sum_1 = total_sum[w-1] - total_sum[z-1]
        if sum_3 > R:
            w = (z+w)//2
        elif sum_3 < R:
            w = (z+N-1)//2
    if sum_3 != R:
        continue
    else:
        print("Yes")
        sys.exit()
        
print("No")
                
