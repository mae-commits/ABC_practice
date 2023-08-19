M = int(input())

D = list(map(int, input().split()))

total_days =sum(D)

days = total_days

half = (days + 1) // 2

i = 0
while days > half:
    days -= D[i]
    i += 1

if total_days == 1:
    print(1, 1)
else:
    if days == half:
        print(i+1, 1)
    else:
        print(i, D[i-1] + (days - half) + 1)