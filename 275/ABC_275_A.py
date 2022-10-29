n = int(input())

h = [0] + list(map(int,input().split()))

max_bridge = 0
max_num = 0

for i in range(len(h)):
    if max(h[i],max_bridge) == h[i]:
        max_bridge = h[i]
        max_num = i
        
print(max_num)