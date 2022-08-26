import sys 

S = input()

for i in range(len(S)):
    letter_count = S.count(S[i])
    if letter_count == 1:
        print(S[i])
        sys.exit()

print(-1)
    
    