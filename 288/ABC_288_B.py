n, k = map(int,input().split())

s = list(input() for i in range(n))

s_win = list(sorted(s[0:k]))
for i in s_win:
    print(i)
