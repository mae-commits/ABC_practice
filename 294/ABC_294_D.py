from collections import deque

N, Q = map(int,input().split())

customer = deque(i+1 for i in range(N))
called = set()

for i in range(Q):
    event = list(map(int,input().split()))
    if event[0] == 1:
        called_customer = customer.popleft()
        called.add(called_customer)
    elif event[0] == 2:
        called.remove(event[1])
    else:
        recalled = deque(called).popleft()
        called = set(called)
        print(recalled)