from collections import deque

n = int(input())

a = deque(map(int,input().split()))

a_odd = []
a_even = []

for i in range(n):
    a_element = a.popleft()
    if a_element % 2 != 0:
        a_odd.append(a_element)
    else:
        a_even.append(a_element)
        
a_odd_sort = sorted(a_odd, reverse = True)
a_even_sort = sorted(a_even, reverse = True)
odd_max_sum = -1
even_max_sum = -1

if len(a_odd_sort) < 2 and len(a_even_sort) < 2:
    print('-1')
else:
    if len(a_odd_sort) >= 2:
        odd_max_sum = a_odd_sort[0] + a_odd_sort[1]
    if len(a_even_sort) >= 2:
        even_max_sum = a_even_sort[0] + a_even_sort[1]
    print(max(odd_max_sum,even_max_sum))