S = list(input())

B_index = []

K_index = []

R_index = []

for i in range(8):
    if S[i] == 'B':
        B_index.append(i+1)
    elif S[i] == 'K':
        K_index.append(i+1)
    elif S[i] == 'R':
        R_index.append(i+1)
        
if B_index[0] % 2 == B_index[1] %2 or K_index[0] < R_index[0] or K_index[0] > R_index[1]:
    print('No')
    exit()
else:
    print('Yes')