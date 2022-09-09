n,x = map(int,input().split())

# Arrange the indices
a = [0] + list(map(int,input().split()))
known = set()
a_i = x

# loop until the next people are already known
while a_i not in known:
    known.add(a_i)
    a_i = a[a_i]

print(len(known))
