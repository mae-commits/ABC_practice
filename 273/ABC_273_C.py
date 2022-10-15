from collections import deque

n = int(input())

a = sorted(list(map(int,input().split())), reverse=True)
a_deq = deque(a)
a_old = 0
k = 0 # numbers more than the selected number
kinds = [0] * n
 
for i in range(n):
    if i == 0:
        kinds[k] += 1
        a_old = a_deq.popleft()
    else:
        a_element = a_deq.popleft()
        # print(a_element, a_old)
        if a_element == a_old:
            kinds[k] += 1
            a_old = a_element
        else:
            a_old = a_element
            k += 1
            kinds[k] += 1

for i in kinds:
    print(i)