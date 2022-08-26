from collections import deque

N = int(input())

A = list(map(int,input().split()))

count = 0
same = 0

for index, num in enumerate(A,1):
    if index == num:
        same += 1

count += same * (same - 1) // 2

for index,num in enumerate(A,1):
    if index < num and A[num-1] == index:
        count += 1

print(count)
