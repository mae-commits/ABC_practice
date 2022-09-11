from collections import deque
from mimetypes import init

n = int(input())

p = list(map(int,input().split()))
#Total enjoy for each rotation.
enjoy = [0]*n

for i in range(len(p)):
    initialPlace = i
    dishNum = p[i]
    if dishNum == n-1:
        if initialPlace <= n-2 and initialPlace > 0:
            enjoy[n-2-initialPlace] += 1
            enjoy[n-1-initialPlace] += 1
            enjoy[n-initialPlace] += 1
        elif initialPlace == 0:
            enjoy[0] += 1
            enjoy[n-2] += 1
            enjoy[n-1] += 1
        else:
            enjoy[0] += 1
            enjoy[1] += 1
            enjoy[n-1] += 1 
    elif dishNum == 0:
        if initialPlace <= n-1 and initialPlace > 1:
            enjoy[n-initialPlace] += 1
            enjoy[n-initialPlace-1] += 1
            enjoy[n-initialPlace+1] += 1
        elif initialPlace == 1:
            enjoy[0] += 1
            enjoy[n-1] += 1
            enjoy[n-2] += 1
        else:
            enjoy[0] += 1
            enjoy[1] += 1
            enjoy[n-1] += 1
    else:
        if dishNum - initialPlace >= 1:
            enjoy[dishNum - initialPlace -1] += 1
            enjoy[dishNum - initialPlace] += 1
            enjoy[dishNum - initialPlace + 1] += 1
        elif dishNum - initialPlace == 0:
            enjoy[dishNum - initialPlace] += 1
            enjoy[dishNum - initialPlace + 1] += 1
            enjoy[n-1] += 1
        elif dishNum - initialPlace == -1:
            enjoy[dishNum - initialPlace + 1] += 1
            enjoy[n-1] += 1
            enjoy[n-2] += 1
        else:
            enjoy[dishNum - initialPlace -1 + n] += 1
            enjoy[dishNum - initialPlace + n] += 1
            enjoy[dishNum - initialPlace + 1 + n] += 1
            
print(max(enjoy))
