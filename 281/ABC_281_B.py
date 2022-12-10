import sys

s = input()

s_first = s[0]

s_num = s[1:-1]

s_last = s[-1]

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if len(s_num) != 6 or s_num.isdecimal() == False or len(s) != 8:
    print("No")
elif int(s_num) < 100000 or int(s_num) > 999999:
    print("No")
elif s_first not in alphabet or s_last not in alphabet:
    print("No")
else:
    print("Yes")
    
    