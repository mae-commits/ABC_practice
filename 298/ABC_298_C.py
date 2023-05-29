N = int(input())

Q = int(input())

boxes = [[] for i in range(N+1)]
box_nums = [set() for i in range(201000)]

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        boxes[query[2]].append(query[1])
        box_nums[query[1]].add(query[2])
    elif query[0] == 2:
        print(*sorted(boxes[query[1]]))
    else:
        print(*sorted(box_nums[query[1]]))