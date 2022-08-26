import sys

H, W = map(int,input().split())

G = list(list(input()) for i in range(H))

# print(G)
G_kinds = ["U", "D", "L", "R"]
x_move = [-1, 1, 0, 0]
y_move = [0, 0, -1, 1]
mark_place = list(list(False for i in range(W)) for j in range(H))
mark_place[0][0] = True
tmp_place = [0,0]

# print(mark_place)

for i in range(10**10):
    ith_move = G[tmp_place[0]][tmp_place[1]] # Resister the letter of movements.
    if ith_move == "U":
        if tmp_place[0] == 0:
            print(str(tmp_place[0]+1), str(tmp_place[1]+1))
            sys.exit()
        else:
            tmp_place[0] += x_move[0]
            tmp_place[1] += y_move[0]
            if mark_place[tmp_place[0]][tmp_place[1]] == True:
                print(-1)
                sys.exit()
            else:
                mark_place[tmp_place[0]][tmp_place[1]] = True
    elif ith_move == "D":
        if tmp_place[0] == H-1:
            print(str(tmp_place[0]+1), str(tmp_place[1]+1))
            sys.exit()
        else:
            tmp_place[0] += x_move[1]
            tmp_place[1] += y_move[1]
            if mark_place[tmp_place[0]][tmp_place[1]] == True:
                print(-1)
                sys.exit()
            else:
                mark_place[tmp_place[0]][tmp_place[1]] = True
    elif ith_move == "L":
        if tmp_place[1] == 0:
            print(str(tmp_place[0]+1), str(tmp_place[1]+1))
            sys.exit()
        else:
            tmp_place[0] += x_move[2]
            tmp_place[1] += y_move[2]
            if mark_place[tmp_place[0]][tmp_place[1]] == True:
                print(-1)
                sys.exit()
            else:
                mark_place[tmp_place[0]][tmp_place[1]] = True
    elif ith_move == "R":
        if tmp_place[1] == W-1:
            print(str(tmp_place[0]+1), str(tmp_place[1]+1))
            sys.exit()
        else:
            tmp_place[0] += x_move[3]
            tmp_place[1] += y_move[3]
            if mark_place[tmp_place[0]][tmp_place[1]] == True:
                print(-1)
                sys.exit()
            else:
                mark_place[tmp_place[0]][tmp_place[1]] = True
    

