N = int(input())

P = list(map(int,input().split()))

P = [0,0] + P

# print(P)
count = 0 # Count the descendents loops.

i = N # Start from N.

while P[i] != 1:
    i = P[i]
    # print(P[i])
    count += 1
    
print(count + 1)