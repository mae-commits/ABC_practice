def price(N):
    # Solve the digit of N.
    N_str = str(N)
    d = len(N_str)
    return A*N + B*d
    
# Input the values from the command line.
A, B, X = map(int,input().split())

if price(1) > X:
    print(0)
else:
    left = 1
    right = 10 ** 20
    while right - left > 1:
        mean = (left + right) // 2
        if price(mean) <= X:
            left = mean
        else:
            right = mean
    if left < 10 ** 9:
        print(left)
    else:
        print(10 ** 9)

