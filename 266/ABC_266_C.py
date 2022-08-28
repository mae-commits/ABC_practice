import math

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))


def vec(a,b):
    return [a[0]-b[0],a[1]-b[1]]

# Pursue crossing line

AC_vec = vec(A,C)

AC_cross_vec = [AC_vec[1], - AC_vec[0]]

BD_vec = vec(B,D)

BD_cross_vec = [BD_vec[1], - BD_vec[0]]

# Detect whether or not the point is above the line.
def up_down(point,base_point, vec):
    return (point[0] - base_point[0]) * vec[0] + (point[1] - base_point[1]) * vec[1]

B_detect = up_down(B,A,AC_cross_vec)

D_detect = up_down(D,A,AC_cross_vec)

A_detect = up_down(A,B,BD_cross_vec)

C_detect = up_down(C,B,BD_cross_vec)

B_D_judge = B_detect * D_detect

A_C_judge = A_detect * C_detect

# print(B_detect)
# print(D_detect)
# print(A_detect)
# print(C_detect)

if B_D_judge < 0 and A_C_judge < 0:
    print("Yes")
else:
    print("No")