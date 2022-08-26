A, B, W = map(int,input().split())

m = 1000 * W / A
M = 1000 * W / B

if int(m) == int(M) and (m != int(m) and M != int(M)):
    print("UNSATISFIABLE")
elif int(m) == m and int(M) == M:
    print(str(int(M)) + " " + str(int(m)))
elif int(m) == m:
    print(str(int(M) + 1) + " " + str(int(m)))
elif int(M) == M:
    print(str(int(M)) + " " + str(int(m) - 1))
else:
    print(str(int(M) + 1) + " " + str(int(m)))
    
    