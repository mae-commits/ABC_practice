s = [0] + list(input())

s_new = []

for i in range(1,len(s)//2 + 1):
    s_new.append(s[2*i])
    s_new.append(s[2*i-1])
    
print("".join(s_new))