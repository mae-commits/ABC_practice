import sys 
n, s = map(int,input().split())

ab = list(list(map(int,input().split())) for i in range(n))

for i in range(1 << n):
    ht = ''
    count = 0
    for j in range(n):
        if i >> j:
            count += ab[j][0]
            ht = ht + 'H'
        else:
            count += ab[j][1]
            ht = ht + 'T'
    if count == s:
        print('Yes')
        print(ht)
        sys.exit()
print('No')