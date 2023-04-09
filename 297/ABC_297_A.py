N, D = map(int,input().split())

T = list(map(int,input().split()))

ans = -1

last_click = 0

i = 1

for present_click in T:
    if i == 1:
        last_click = present_click
    elif present_click - last_click <= D:
        print(present_click)
        exit()
    last_click = present_click
    i += 1

print(-1)