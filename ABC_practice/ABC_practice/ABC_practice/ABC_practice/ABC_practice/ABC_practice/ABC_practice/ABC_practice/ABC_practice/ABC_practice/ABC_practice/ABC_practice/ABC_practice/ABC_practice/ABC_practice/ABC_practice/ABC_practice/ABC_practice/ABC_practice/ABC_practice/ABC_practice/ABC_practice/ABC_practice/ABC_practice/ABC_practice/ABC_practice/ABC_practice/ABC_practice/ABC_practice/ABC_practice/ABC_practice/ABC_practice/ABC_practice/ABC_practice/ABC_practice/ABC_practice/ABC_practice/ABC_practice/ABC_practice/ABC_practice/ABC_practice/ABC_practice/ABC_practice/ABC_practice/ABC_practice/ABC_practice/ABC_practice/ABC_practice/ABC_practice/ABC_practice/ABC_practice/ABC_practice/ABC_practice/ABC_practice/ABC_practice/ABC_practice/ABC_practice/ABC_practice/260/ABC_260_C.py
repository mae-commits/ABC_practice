"""
This code aims to calculate the maximum number of blue stones.
Take advantage of calculation "Dynamic Planning (DP)."
"""
N,X,Y = map(int,input().split())

"""
define the list about the number of blue/red stones.
r[i]: the number of Lv.1's blue stones, starting from one Lv.i's red stones. 
b[i]: the number of Lv.1's blue stones, starting from one Lv.i's blue stones.
"""
r = [0]*12
b = [0]*12

"""
r[1] is of course 0, and b[i] is of course 1.
"""

r[1] = 0
b[1] = 1

"""
Calculate the number of stones for each color from lower level 
"""
for i in range(2,N+1):
    b[i] = r[i-1] + b[i-1] * Y
    r[i] = r[i-1] + b[i] * X
print(r[N])
