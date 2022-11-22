n, q = map(int,input().split())

follow_list = set()
ans = []

for i in range(q):
    t, a, b = map(int,input().split())
    if t == 1:
        follow_list.add(str(a) + str(b))
    elif t == 2:
        if (str(a) + str(b)) in follow_list:
            follow_list.remove(str(a) + str(b))
    else:
        if (str(a) + str(b)) in follow_list and (str(b) + str(a)) in follow_list:
            ans.append('Yes')
        else:
            ans.append('No')

for i in range(len(ans)):
    print(ans[i])