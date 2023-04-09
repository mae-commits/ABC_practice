H, W = map(int,input().split())

S = list(input() for i in range(H))

new_S = []

changed = False

for line in S:
    last_letter = ''
    new_S_line = []
    for i in range(W):
        if changed == False and last_letter == 'T' and line[i] == 'T':
            new_S_line[-1] = 'P'
            new_S_line.append('C')
            changed = True
        else:
            new_S_line.append(line[i])
            changed = False
            last_letter = line[i]
    new_S.append(''.join(new_S_line))

for new_line in new_S:
    print(new_line)
