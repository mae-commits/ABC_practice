x,k = map(int,input().split())

for i in range(k):
    length = len(str(x))
    rest = x% (10 ** (i+1))
    top_rest = int(str(rest)[0])
    if top_rest >= 5:
        x += (10 ** (i+1) - top_rest * (10 ** i))
    else:
        x -= top_rest * (10 ** i)

print(x)
        