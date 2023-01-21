n, p, q, r, s = map(int,input().split())

a = [0] + list(map(int,input().split())) + [0]

b = a[0:p] + a[r:s+1] + a[q+1:r] + a[p:q+1] + a[s+1:n+1]

print(*b[1:n+1])