import itertools

s = [list(input()) for i in range(9)]

count_porn = []

for i in range(9):
    for j in range(9):
        if s[i][j] == '#':
            count_porn.append([i,j])

count_square = 0
count_num = set()
t = list(itertools.combinations(range(len(count_porn)),2))

def judge1(a, b, x_1, y_1):
    return [[x_1-b,y_1+a],[x_1+(a-b),y_1+(a+b)]]

def judge2(a, b, x_1, y_1):
    return [[x_1+b,y_1-a],[x_1-(a-b),y_1-(a+b)]]

for i in t:
    first_point_num = i[0]
    second_point_num = i[1]
    first_point = count_porn[first_point_num]
    second_point = count_porn[second_point_num]
    x_1, y_1 = first_point[0], first_point[1]
    a = second_point[0] - first_point[0]
    b = second_point[1] - first_point[1]
    other_points = judge1(a, b, x_1, y_1)
    count = 0
    points_num = []
    for j in range(len(count_porn)):
        if count_porn[j] == other_points[0] or count_porn[j] == other_points[1]:
            count += 1
            points_num.append(j)
        if count == 2:
            j1 = points_num[0]
            j2 = points_num[1]
            count_square += 1
            points_list = sorted([first_point_num,second_point_num,j1,j2])
            num = str(points_list[0]) + str(points_list[1]) + str(points_list[2]) + str(points_list[3])
            count_num.add(num)
        
# print(list(count_num))
print(len(count_num))