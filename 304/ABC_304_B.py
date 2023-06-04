N = input()

if len(N) <= 2:
    print(int(N))
else:
    print(int(N[0:3]) * 10 ** (len(N)-3))