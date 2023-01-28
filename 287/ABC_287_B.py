n, m = map(int,input().split())

s = list(input() for i in range(n))

t = list(input() for i in range(m))

count = 0

for i in s:
    for j in t:
        if i[3::] == j:
            count += 1
            break

print(count)