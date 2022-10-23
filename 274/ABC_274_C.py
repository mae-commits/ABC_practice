n = int(input())

a = list(map(int, input().split()))

childs = [0 for i in range(2*n+2)]

for i in range(n):
    child_1 = 2*(i+1)
    child_2 = 2*(i+1) + 1
    count = childs[a[i]]
    childs[child_1] = count + 1
    childs[child_2] = count + 1
    
for i in childs[1:]:
    print(i)