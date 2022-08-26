L_1,R_1,L_2,R_2 = map(int,input().split())

if R_1 <= L_2 or R_2 <=  L_1:
    print(0)
elif R_1 >= R_2:
    print(min(abs(R_2 - L_1), abs(R_2 -L_2)))
elif R_1 <= R_2:
    print(min(abs(R_1 - L_1),abs(R_1 - L_2)))
