x, y, z = map(int,input().split())

x = x + 1000
y = y + 1000
z = z + 1000

if x > 1000:
    if y > x or y < 1000:
        print(x-1000)
    elif y < x and y > 1000:
        if z > y:
            print(-1)
        elif z < 1000:
            print(1000 - z + x - z)
        else:
            print(x - 1000)
else:
    if y < x or y > 1000:
        print(1000-x)
    elif y > x and y < 1000:
        if z < y:
            print(-1)
        elif z > 1000:
            print(z-1000 + z - x)
        else:
            print(1000-x)