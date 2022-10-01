from collections import deque
import sys

n = int(input())

a = sorted(list(map(int,input().split())))
a_deq = deque(a)

if n == 1:
    if a[0] != 1:
        print(0)
        sys.exit()
    else:
        print(1)
        sys.exit()
else:
    book_rest = n
    for i in range(n):
        original = a_deq.popleft()
        dif = original - (i+1)
        book_rest = book_rest - div 
        book_rest -= 1
        if book_rest <= 0:
            print(i+1)
            sys.exit()
        elif book_rest == 1:
            original = a_deq.popleft()
            ideal = a_ideal.popleft()
            print(i+2)
            sys.exit()
print(n)