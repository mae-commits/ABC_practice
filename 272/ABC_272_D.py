from collections import deque

n, m = map(int,input().split())

numbers = [[-1 for i in range(n+1)] for j in range(n+1)]

def judge_squared_distance(original_point,candidate_point, m):
    i, j = original_point[0], original_point[1]
    k, l = candidate_point[0], candidate_point[1]
    if (i-k) ** 2 + (j-l) ** 2 == m and numbers[k][l] == -1:
        return True
    else:
        return False

que = deque()

que.append([1,1])
numbers[1][1] = 0

while len(que) > 0:
    original_point = que.popleft()
    compiled_sum =numbers[original_point[0]][original_point[1]]
    for i in range(1,n+1):
        for j in range(1,n+1):
            candidate_point = [i, j]
            if candidate_point not in que:
                if judge_squared_distance(original_point, candidate_point, m) == True:
                    que.append(candidate_point)
                    numbers[i][j] = compiled_sum + 1

for i in range(1,n+1):
    print(*numbers[i][1:])