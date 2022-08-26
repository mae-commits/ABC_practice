import sys

S = str(input())

T = "oxx" * 100

if S in T:
    print("Yes")
else:
    print("No")



"""
count_o = 0
count_x = 0 

for i in range(len(S)):
    if S[i] == "o":
        count_x = 0
        count_o += 1
        if count_o >= 2:
            print("No")
            sys.exit()
    else:
        count_x += 1
        count_o = 0
        if count_x >= 3:
            print("No")
            sys.exit()

print("Yes")
""" 
