s = input()

cup_num = 0

for i in range(len(s)):
    if s[i] == 'v':
        cup_num+=1
    elif s[i] == 'w':
        cup_num+=2

print(cup_num)