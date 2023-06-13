from bisect import bisect_left

N = int(input())

A = list(map(int, input().split()))

sleep = [0]*N

# 就寝・起床時間時点で何時間寝たかの累積和
for i in range(1, N):
    if i % 2 == 0:
        sleep[i] = sleep[i-1] + A[i] - A[i-1]
    else:
        sleep[i] = sleep[i-1]

Q = int(input())

# 各クエリの処理
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
        minus += l - A[l_index]
    if r_index %2 == 1:
        minus -= r - A[r_index]
    minute = sleep[r_index] - sleep[l_index] - minus
    print(minute)