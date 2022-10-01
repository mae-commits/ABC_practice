a, b = map(int,input().split())

question = [False, False, False]

if a%2 == 1 or b%2 == 1:
    question[0] = True
    if a%2 == 1:
        a-=1
    if b%2 == 1:
        b-=1
        
if (a != 0 and (a == 4 or a == 6)) or (b != 0 and (b == 4 or b == 6)):
    question[2] = True
    if a != 0 and (a == 4 or a == 6):
        a-= 4
    if b != 0 and (b == 4 or b == 6):
        b-= 4

if (a%2 == 0 and a != 0) or (b%2 == 0 and b != 0):
    question[1] = True
    if a%2 == 0:
        a-=2
    if b%2 == 0:
        b-=2

points = [1,2,4]
ans = 0

for i in range(3):
    if question[i] == True:
        ans += points[i]

print(ans)