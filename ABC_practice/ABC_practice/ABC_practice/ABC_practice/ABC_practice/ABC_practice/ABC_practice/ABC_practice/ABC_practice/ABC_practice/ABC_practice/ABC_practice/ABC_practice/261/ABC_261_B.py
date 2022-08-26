import sys

N = int(input())

A = list(input() for i in range(N))

for i in range(N):
    for j in range(N):
        if i != j:
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                sys.exit()
            elif A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                sys.exit()
            elif A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                sys.exit()

print("correct")