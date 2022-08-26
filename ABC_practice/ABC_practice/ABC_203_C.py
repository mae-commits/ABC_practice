# from collections import deque

N,K = map(int,input().split())

friends_list = list(list(map(int,input().split())) for i in range(N))

village = 0

friends_list.sort()

village += K

for i in range(N):
    friends_village = friends_list[i][0]
    friends_money = friends_list[i][1]
    
    if friends_village <= village:
        village+= friends_money
    else:
        break
print(village)