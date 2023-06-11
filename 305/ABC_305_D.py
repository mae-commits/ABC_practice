from bisect import bisect_left

N = int(input())

A = list(map(int, input().split()))

sleep = [0]

for i in range(N):
    if i % 2 != 0:
        sleep.append(A[i+1] - A[i])
    else:
        sleep.append(0)

Q = int(input())
dif = []

for i in range(Q):
    l, r = map(int, input().split())
    r_index = bisect_left(A, r)
    l_index = bisect_left(A, l)
    minute = 0
    minus = 0
    A_r, A_l = A[r_index], A[l_index]
    if A_r != r:
        r_index -= 1
    if A_l != l:
        l_index -= 1
    if l_index %2 == 1:
        minus += l - A_l
    if r_index %2 == 1:
        minus -= r - A_r
    start = l_index if l_index %2 == 1 else l_index + 1
    end = r_index if r_index %2 == 1 else r_index + 1
    minute = sum(sleep[start:end+1]) - minus
    dif.append(minute)

for i in range(Q):
    print(dif[i])