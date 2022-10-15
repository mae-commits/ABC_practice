from collections import deque

# [r_s, c_s]: initial place
#h, w : the range of grids
h,w,r_s,c_s = map(int,input().split())
r_tmp, c_tmp = r_s, c_s
n = int(input())

blocks = []

for i in range(n):
    blocks.append([map(int,input().split())])

q = int(input())

queues = deque()

for i in range(q):
    queues.append([map(str,input().split())])


for i in range(q):
    d, l = queues.popleft()
    l = int(l)
    if d == 'L':
        r_tmp -= l
        if r_tmp < 1:
            r_tmp = 1
        if c_tmp in blocks[]:
        
    elif d == 'R':
        