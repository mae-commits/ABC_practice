n, x, y = map(int,input().split())

a = list(map(int,input().split()))

a_even = []
a_odd = []

for i in range(len(a)):
    if (i+1)%2 == 0:
        a_even.append(a[i])
    else:
        a_odd.append(a[i])

if (n+1)%2 == 0:
    even_loop = (n+1)//2
    odd_loop = (n+1)//2
else:
    even_loop = (n+1)//2
    odd_loop = (n+2)//2
    
dp_x = [[0,0]for i in range(even_loop)]
dp_y = [[0,0]for i in range(odd_loop)]

judge = 
for i in range():