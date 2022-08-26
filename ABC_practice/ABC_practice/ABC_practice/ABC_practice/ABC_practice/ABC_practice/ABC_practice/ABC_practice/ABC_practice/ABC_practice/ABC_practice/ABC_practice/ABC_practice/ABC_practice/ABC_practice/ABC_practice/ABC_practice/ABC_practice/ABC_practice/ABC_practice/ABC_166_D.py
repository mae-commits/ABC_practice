import sys
X = int(input())

for A in range(10**3+1):
    for B in range(-10**3, 10**3+1):
        if A**5 - B**5 == X:
            print(str(A) + " " + str(B))
            sys.exit()

