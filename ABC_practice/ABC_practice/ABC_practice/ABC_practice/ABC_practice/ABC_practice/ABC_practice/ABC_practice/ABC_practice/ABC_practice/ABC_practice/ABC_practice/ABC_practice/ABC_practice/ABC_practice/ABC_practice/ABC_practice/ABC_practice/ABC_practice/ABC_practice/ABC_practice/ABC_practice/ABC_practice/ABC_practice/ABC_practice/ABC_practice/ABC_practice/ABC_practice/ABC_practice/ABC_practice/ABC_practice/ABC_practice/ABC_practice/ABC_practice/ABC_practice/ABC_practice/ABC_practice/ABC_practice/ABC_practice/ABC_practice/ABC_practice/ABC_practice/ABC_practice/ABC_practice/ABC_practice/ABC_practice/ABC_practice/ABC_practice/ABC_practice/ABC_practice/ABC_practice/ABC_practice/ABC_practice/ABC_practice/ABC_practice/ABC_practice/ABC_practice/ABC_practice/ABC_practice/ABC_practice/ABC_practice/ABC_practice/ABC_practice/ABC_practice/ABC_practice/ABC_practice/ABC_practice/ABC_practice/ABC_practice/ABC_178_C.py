N = int(input())

mod = 10**9+7

cnt = pow(10,N,mod)

extract = pow(9,N,mod)

over_extract = pow(8,N,mod)
print((cnt-extract*2+over_extract)%mod)
