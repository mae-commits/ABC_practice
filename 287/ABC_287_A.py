n = int(input())

s = list(input() for i in range(n))

count = 0

for i in s:
    if i == "For":
        count+=1

if count > n//2:
    print("Yes")
else:
    print("No")