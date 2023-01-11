n = int(input())

s = list(input() for i in range(n))

for i in range(n):
    print(s[n-1-i])