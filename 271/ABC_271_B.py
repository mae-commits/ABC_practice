n,q = map(int,input().split())

sequences = [[]]

for i in range(n):
    sequences_i = list(map(int,input().split()))
    sequences.append(sequences_i)
    
s_t = []
for i in range(q):
    s_t_i = list(map(int,input().split()))
    s_t.append(s_t_i)
    
for i in range(q):
    print(sequences[s_t[i][0]][s_t[i][1]])