N, M, T = map(int,input().split())

import sys
# The time Takahashi spend movement from i th to i+1 th room.
A = list(map(int,input().split()))

bonus = [0 for i in range(N)]

for i in range(M):
    X, Y = map(int,input().split())
    bonus[X-1] = Y

rest_time = T

for i in range(N-1):
    rest_time -= A[i]
    if rest_time <= 0:
        print("No")
        sys.exit()
    rest_time += bonus[i+1]
    # print(rest_time)
    
print("Yes")
    