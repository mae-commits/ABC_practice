def binary_search(N, M):
    left = M
    right = N ** 2
    X = (left + right) // 2
    if M <= N:
        return M
    for i in range(2, N//2 + 1):
        if X % i == 0:
            return X
    if (N//2) ** 2 <= X:
        left = X
    else:
        right = X
    if left == right:
        return -1
    
N, M = map(int, input().split())

if M > N ** 2:
    print("No")

X = binary_search(N, M)

print(X)