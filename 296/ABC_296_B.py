S = list(list(input()) for i in range(8))

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(chr(j+97)+str(8-i))