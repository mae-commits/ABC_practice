N, M = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = list(map(int,input().split()))

score = 0

for num in B:
    score+=A[num]

print(score)