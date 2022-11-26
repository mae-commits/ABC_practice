import sys
s = input()
t = input()

len_s = len(s)
len_t = len(t)
dif = len_s - len_t

if len(s) < len(t):
    print('No')
    sys.exit()
for i in range(dif+1):
    if s[i:i+len_t] == t:
        print('Yes')
        sys.exit()
        
print('No')