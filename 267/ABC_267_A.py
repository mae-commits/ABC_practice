import sys

S = input()

day = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]

for i in range(len(day)):
    if S == day[i]:
        print(5-i)
        sys.exit()
