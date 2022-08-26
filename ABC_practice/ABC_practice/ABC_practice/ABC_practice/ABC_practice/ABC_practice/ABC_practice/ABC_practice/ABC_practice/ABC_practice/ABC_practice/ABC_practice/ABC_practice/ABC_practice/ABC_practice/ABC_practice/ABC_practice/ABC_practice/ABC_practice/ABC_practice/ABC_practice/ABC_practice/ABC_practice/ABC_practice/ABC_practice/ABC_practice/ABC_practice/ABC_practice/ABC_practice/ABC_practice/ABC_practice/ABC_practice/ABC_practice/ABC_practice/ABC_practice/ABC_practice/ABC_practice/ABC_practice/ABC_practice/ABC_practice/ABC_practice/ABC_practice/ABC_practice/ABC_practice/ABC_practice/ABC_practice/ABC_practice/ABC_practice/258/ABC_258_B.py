N = int(input())

A = list((input()for i in range(N)))

A_new = ["0" for i in range(N)]

for i in range(N):
    A_new[i] = A[i] * 3

for i in range(2):
    for j in range(N):
        A_new.append(A_new[j])

dir_x = [0,1,1,1,0,-1,-1,-1]
dir_y = [-1,-1,0,1,1,1,0,-1]

num = 0

for i in range(N):
    for j in range(N):  
        x_pro = i+N
        y_pro = j+N
        for l in range(8):
            num_arange = A_new[i+N][j+N] # decide the first index
            for k in range(N-1):
                num_arange = num_arange + A_new[x_pro + dir_x[l] * (k+1)][y_pro + dir_y[l] * (k+1)]
                # print(num_arange)
                num = max(int(num_arange),int(num))

print(num)

