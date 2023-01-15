n = int(input())
s = ['0'] + list(input())
l = [0]*(n+1)

for i in range(1,n):
    count=0
    j=1
    while s[j] != s[i+j] and i+j < n:
        count=j
        j+=1
    l[i]=count
        
for i in range(1,n):
    print(l[i])