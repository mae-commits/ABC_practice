import itertools

h, w = map(int,input().split())

a = list(list(map(int,input().split())) for i in range(h))

count = 0

arr = [True for i in range(h-1)]

arr = arr + [False for i in range(w-1)]

p = itertools.permutations(arr, h+w-2)

route = set([a[0][0]])

first_state = a[0][0]

for v in p:
    vertical = 0
    horizontal = 0
    route = set([first_state])
    for verify in v:
        if verify == True:
            # print(a[vertical+1][horizontal])
            vertical+=1
            route.add(a[vertical][horizontal])
        else:
            # print(a[vertical][horizontal+1])
            horizontal+=1
            route.add(a[vertical][horizontal])
        # print(vertical, horizontal)
    # print(route)
    if len(route) == h+w-1:
        count+=1

print(count)