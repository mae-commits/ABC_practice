h, m = map(int,input().split())

time = h * 100 + m

mistaken_time = False

while mistaken_time == False:
    if time <= 1000:
        len_time = len(str(time))
        for i in range(4 - len_time):
            time =  str(0) + str(time)
    exchange_time = str(int(str(time)[0]) * 1000 + int(str(time)[2])*100 + int(str(time)[1])*10 + int(str(time)[3]))
    # print(exchange_time)
    if int(exchange_time) < 2400 and int(exchange_time) % 100 < 60:
        mistaken_time = True
    else:
        time = int(time) + 1
        if time%100 >= 60:
            time = time//100 * 100 + 100
        if time >= 2400:
            time = 0

print(str(time)[0:2] + " " + str(time)[2:4])