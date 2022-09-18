S = list(input() for i in range(10))
A,B,C,D = -1,-1,-1,-1

mark_line = False
mark_low = False

for i in range(10):
    for j in range(len(S)):
        if '#' not in S[i] and (mark_line == True and mark_low == False):
            mark_line = False
            B = i
        if S[i][j] == '#' and (mark_line == False and mark_low == False):
            mark_line = True
            mark_low = True
            C = j+1
            A = i+1
        if S[i][j] == '.' and (mark_line == True and mark_low == True):
            mark_low = False
            D = j
        if S[i][j] == '#' and j == 9:
            mark_line = True
            mark_low = False
            D = 10
        
if B == -1 and A != -1:
    B = 10
if D == -1 and C != -1:
    D = 10

print(str(A)+ ' ' + str(B))
print(str(C)+ ' ' + str(D))