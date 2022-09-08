a, b = map(str,input().split())
#Separate the number as list elememts
aList = list(reversed(list(a)))
bList = list(reversed(list(b)))

for i in range(min(len(a),len(b))):
    if int(aList[i]) + int(bList[i]) >= 10:
        print('Hard')
        exit()

print('Easy')