a, b, c, d, e, f = map(int,input().split())

div = 998244353

a = a%div
b = b%div
c = c%div
d = d%div
e = e%div
f = f%div

a_b_c = (((a*b)%div)*c)%div
d_e_f = (((d*e)%div)*f)%div

if a_b_c < d_e_f:
    print(a_b_c - d_e_f + div)
else:
    print(a_b_c - d_e_f)