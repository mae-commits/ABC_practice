s1 = input()
s2 = input()

countBlack = s1.count('#') + s2.count('#')

if countBlack == 2:
    if s1[0] == '#' and s2[0] == '#':
        print('Yes')
    elif s1[1] == '#' and s2[1] == '#':
        print('Yes')
    elif s1.count('#') == 2 or s2.count('#') == 2:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')