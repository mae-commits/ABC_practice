n = int(input())

s = list(map(int,input().split()))

estimatedSpace = set()

for a in range(1,201):
    for b in range(1,201):
        if 4 * a * b + 3 * a + 3 * b <= 1000:
            estimatedSpace.add(4 * a * b + 3 * a + 3 * b)

count = 0

for i in range(n):
    if s[i] not in estimatedSpace:
        count += 1

print(count)