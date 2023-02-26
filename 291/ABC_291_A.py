import sys

s = list(input())

count = 1
for letter in s:
    if letter.islower() == True:
        count+=1
        continue
    else:
        print(count)
        sys.exit()

