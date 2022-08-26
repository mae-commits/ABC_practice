N = int(input())

if N <= 41:
    N = "0" * (3-len(str(N))) + str(N)
    print("AGC" + N)
else:
    N = "0" * (3-len(str(N+1))) + str(N+1)
    print("AGC" + N)
