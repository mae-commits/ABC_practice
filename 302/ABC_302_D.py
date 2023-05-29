from collections import deque as d

N, M, D = map(int, input().split())

A = d(sorted(list(map(int, input().split()))))
B = d(sorted(list(map(int, input().split()))))

ans = -1
A_max = A.pop()
B_max = B.pop()

while True:
    if abs(A_max - B_max) <= D:
        ans = A_max + B_max
        break
    elif A_max > B_max:
        if len(A) >= 1:
            A_max = A.pop()
        else:
            break
    elif A_max < B_max:
        if len(B) >= 1:
            B_max = B.pop()
        else:
            break
print(ans)