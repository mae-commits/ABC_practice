s = list(input())
s_new = ""

for i in s:
    if i == "0":
        s_new+="1"
    else:
        s_new+="0"
print(s_new)