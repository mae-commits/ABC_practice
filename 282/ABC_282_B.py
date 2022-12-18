n, m = map(int,input().split())

s = list(list(input()) for i in range(n))

count = 0

for i in range(n-1):
    for j in range(i+1,n):
        all = True
        for k in range(m):
            if s[i][k] != 'o' and s[j][k] != 'o':
                all = False
                break
        if all == True:        
            count+=1

print(count)