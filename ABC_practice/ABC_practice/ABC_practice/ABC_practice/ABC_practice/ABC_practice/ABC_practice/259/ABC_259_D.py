N = int(input())
# input the initial and last point.
sx,sy,tx,ty = map(int,input().split())
# input points and circles. 
points = list(list(map(int,input().split())) for i in range(N))

s_circle = [] # circle the initial point exists on. 

t_circle = [] # circle the last point exists on.

