from collections import deque

q = int(input())

a = deque()
ith_a_tail = deque()
note = [[] for i in range(10 ** 9 + 1)]
queries = deque()
for i in range(q):
    query_i = list(input())
    queries.append(query_i)

for i in range(q):
    query_raw = queries.popleft()
    comment,number = map(str, query_raw.split())
    number = int(number)
    if comment == 'ADD':
        a.append(number)
        ith_a_tail.append(number)
    elif comment == 'DELETE' and len(a) > 0:
        a.pop()
        tail = a.pop()
        ith_a_tail.append(tail)
        a.append(tail)
    elif comment == 'SAVE':
        note[number] = list(a)
        tail = a.pop()
        ith_a_tail.append(tail)
        a.append(tail)
    elif comment == 'LOAD':
        a = note[number]
        tail = a.pop()
        ith_a_tail.append(tail)
        a.append(tail)

print(*ith_a_tail)

