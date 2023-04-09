import sys

N = int(input())

S = list(input())

last = ""
now = ""

for i in S:
    if now == "":
        now = i
    else:
        now = i
        if last == now:
            print("No")
            sys.exit()
    last = i
print("Yes")