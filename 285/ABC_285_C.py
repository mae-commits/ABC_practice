s = list(input())

count=0

length = len(s)

for i in range(length):
    count+=(ord(s[i])-64)*(26**(length-i-1))

print(count)