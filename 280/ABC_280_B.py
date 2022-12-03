n = int(input())

s = list(map(int,input().split()))

a = []

for i in range(len(s)):
    if i == 0:
        a.append(s[i])
    else:
        a.append(s[i]-s[i-1])

print(*a)