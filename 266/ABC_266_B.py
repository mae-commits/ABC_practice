N = int(input())

div = 998244353

N_div = abs(N)%div

if N >= 0:
    print(N_div)
elif N < 0 and N_div != 0:
    print(div - N_div)
else:
    print(0)