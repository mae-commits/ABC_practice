import sys

N = int(input())

W = list(map(str, input().split()))

judge = ["and", "not", "that", "the", "you"]

for word in W:
    if word in judge:
        print("Yes")
        sys.exit()

print("No")