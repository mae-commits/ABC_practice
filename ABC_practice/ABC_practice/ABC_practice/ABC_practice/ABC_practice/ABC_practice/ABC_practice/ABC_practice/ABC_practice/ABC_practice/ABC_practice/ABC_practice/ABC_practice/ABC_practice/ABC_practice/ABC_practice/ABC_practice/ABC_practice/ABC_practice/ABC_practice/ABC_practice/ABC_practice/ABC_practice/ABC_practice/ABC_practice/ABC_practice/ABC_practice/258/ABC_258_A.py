K = int(input())
K_rest = 0
hour = 21
minute = 0
if K >= 60:
    K_rest = K-60
    print("22:" + "0"*(2-len(str(K_rest))) + str(K_rest))
else:
    print("21:" + "0" * (2-len(str(K))) + str(K))

