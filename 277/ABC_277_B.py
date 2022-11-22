import sys

n = int(input())

s = list(input() for i in range(n))

set_s = set(s)
if len(set_s) != n:
    print('No')
    sys.exit()
else:
    for i in range(n):
        if s[i][0] != 'H' and s[i][0] != 'D' and s[i][0] != 'C' and s[i][0] != 'S':
            print('No')
            sys.exit()
        if s[i][1] != 'A' and s[i][1] != '2' and s[i][1] != '3' and s[i][1] != '4' and s[i][1] != '5' and s[i][1] != '6' and s[i][1] != '7' and s[i][1] != '8' and s[i][1] != '9' and s[i][1] != 'T' and s[i][1] != 'J' and s[i][1] != 'Q' and s[i][1] != 'K':
            print('No')
            sys.exit()
print('Yes')    