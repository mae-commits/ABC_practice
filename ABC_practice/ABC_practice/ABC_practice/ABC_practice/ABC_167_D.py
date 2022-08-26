N, K = map(int,input().split())

A = [0] + list(map(int,input().split()))

# Mark the already visited towns.
visited = [-1]*(N+1)

# The initial town is 1, 
# that is why the initial index of the list "visited" changes the value 0,
# which means the number of movement for the first reach of the town 1.
visited[1]=0

move_cnt = 0

now_town = 1

for i in range(10**6):
    move_cnt += 1
    now_town = A[now_town]
    if move_cnt == K:
        print(now_town)
        exit()
    if visited[now_town] == -1:
        visited[now_town] = move_cnt
    # Otherwise, the town is already visited town,
    else:
        cycle = move_cnt - visited[now_town]
        # Break the loop and resister the starting point of the cycle.
        break

# Extract the move_cnt which is the out side of the cycle.
K -= move_cnt

# Solve the rest of the K/cycle.
K %= cycle

for i in range(K):
    now_town = A[now_town]

print(now_town)



