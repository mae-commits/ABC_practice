from collections import deque
import numpy as np

n, k = map(int,input().split())

a = [0] + list(map(int,input().split()))

a = np.array(a)

q = int(input())

for i in range(q):
    l,r = map(int,input().split())
    a_part = np.array([])
    for j in range(l,r+1-k):
        if j == l:
            a_part = a[j:j+k]
            a_part = a_part - a_part[0]
            # print(a_part)
        else:
            a_part = a_part[1::]
            a_part = np.append(a_part,a[j+k-1])
            a_part = a_part - a_part[0]
            # print(a_part)
    if np.array_equal(a_part,np.zeros(k)) == False:
        # print(a_part)
        print("No")
    else:
        # print(a_part)
        print("Yes")
