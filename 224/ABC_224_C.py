N = int(input())

coordinates = list(list(map(int,input().split())) for _ in range(N))

count = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            first_point = coordinates[i]
            second_point = coordinates[j]
            third_point = coordinates[k]
            vector_1 = [second_point[0]-first_point[0], second_point[1]-first_point[1]]
            vector_2 = [third_point[0]-first_point[0], third_point[1]-first_point[1]]
            if vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0] != 0:
                count += 1
                
print(count)