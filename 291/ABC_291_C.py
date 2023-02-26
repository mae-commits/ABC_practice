from collections import deque

n = int(input())

s = deque(list(input()))

coordinates = set()

last_coordinate_x = "0"
last_coordinate_y = "0"

new_coordinate_x = "0"
new_coordinate_y = "0"

new_coordinate = new_coordinate_x+new_coordinate_y
coordinates.add(new_coordinate)

for i in range(n):
    s_i = s.popleft()
    if s_i == "R":
        new_coordinate_x = str(int(last_coordinate_x)+1)
        new_coordinate_y = last_coordinate_y
        new_coordinate = new_coordinate_x+new_coordinate_y
        coordinates.add(new_coordinate)
    elif s_i == "L":
        new_coordinate_x = str(int(last_coordinate_x)-1)
        new_coordinate_y = last_coordinate_y
        new_coordinate = new_coordinate_x+new_coordinate_y
        coordinates.add(new_coordinate)
    elif s_i == "U":
        new_coordinate_x = last_coordinate_x
        new_coordinate_y = str(int(last_coordinate_y)+1)
        new_coordinate = new_coordinate_x+new_coordinate_y
        coordinates.add(new_coordinate)
    else:
        new_coordinate_x = last_coordinate_x
        new_coordinate_y = str(int(last_coordinate_y)-1)
        new_coordinate = new_coordinate_x+new_coordinate_y
        coordinates.add(new_coordinate)
    # Update coordinates
    last_coordinate_x,last_coordinate_y = new_coordinate_x,new_coordinate_y
    # print(new_coordinate)

# print(coordinates)
if len(coordinates) != n+1:
    print("Yes")
else:
    print("No")