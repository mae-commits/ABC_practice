R, C = map(int,input().split())

walls = list(list(input()) for i in range(R))

for line in range(R):
    for row in range(C):
        if walls[line][row] != "." and walls[line][row] != "#":
            attack = int(walls[line][row])
            for i in range(attack+1):
                for j in range(attack+1-i):
                    if i != 0 or j != 0:
                        if line-i >= 0 and row-j >= 0:
                            if walls[line-i][row-j] == "#":
                                walls[line-i][row-j] = "."
                        if line+i <= R-1 and row-j >= 0:
                            if walls[line+i][row-j] == "#":
                                walls[line+i][row-j] = "."
                        if line-i >= 0 and row+j <= C-1:
                            if walls[line-i][row+j] == "#":
                                walls[line-i][row+j] = "."
                        if line+i <= R-1 and row+j <= C-1:
                            if walls[line+i][row+j] == "#":
                                walls[line+i][row+j] = "."
            walls[line][row] = "."


for line in range(R):
    print("".join(walls[line]))