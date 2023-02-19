from collections import deque as d

import sys


N, K = map(int,input().split())

A = set(map(int,input().split()))

sampleList = set(list(i for i in range(K+1)))


# print(sampleList)
# print(A)
# print(sorted(list(sampleList-A)))

if len(list(sampleList-A)) == 0:
    print(K)
else:
    print(sorted(list(sampleList-A))[0])

# kthList = d(A[:K])

# sampleList = set(list(i for i in range(K+1)))

# rest = d(A[K:])

# m = 0

# if N == K:
#     diffList = list(set(kthList)^sampleList)
#     m = diffList[0]
#     print(m)
#     sys.exit()

# for i in range(N-K):
#     kthList.pop()
#     kthList.append(rest.pop())
#     diffList = list(set(kthList)^sampleList)
#     print(diffList[0])
#     m = max(diffList[0], m)

# print(m)