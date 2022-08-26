Y = int(input())

if Y%4 == 2:
    print(Y)
elif Y%4 == 1:
    print(Y + 1)
elif Y%4 == 3:
    print(Y + 3)
else:
    print(Y + 2)
