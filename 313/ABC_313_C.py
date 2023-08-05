# 入力を受け取る
N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0
# print(sum(A)//N)
if N == 1:
    print(0)
else:
    average = sum(A) // N
    rest = sum(A) % N
    A = sorted([A[i] for i in range(N-rest)] + [A[-(i+1)]-1 for i in range(rest)])
    i = 0
    while A[i] < average:
        ans += average - A[i]
        i += 1
    print(ans)