from collections import deque

N, M = map(int,input().split())

sequences_A = deque(list(map(int,input().split())))
sequences_B = deque(list(map(int,input().split())))

order_A_in_C = deque()
order_B_in_C = deque()

count = 1
last_num = 0
A_num = 0
B_num = 0

# count_A = 0
# count_B = 0

len_count_A = 0
len_count_B = 0

while count <= N+M-1:
    if last_num == 0:
        A_num = sequences_A.popleft()
        B_num = sequences_B.popleft()
        # count_A+=1
        # count_B+=1
    elif last_num == 1 and len_count_A <= N-1:
        A_num = sequences_A.popleft()
        # count_A+=1
    elif last_num == 2 and len_count_B <= M-1:
        B_num = sequences_B.popleft()
        # count_B+=1
        
    if A_num < B_num and len_count_A<N:
        last_num = 1
        order_A_in_C.append(count)
        len_count_A+=1
    elif A_num > B_num and len_count_B<M:
        last_num = 2
        order_B_in_C.append(count)
        len_count_B+=1
    elif A_num < B_num:
        last_num = 2
        order_B_in_C.append(count)
        len_count_B+=1
    else:
        last_num = 1
        order_A_in_C.append(count)
        len_count_A+=1
    count+=1
    # print(count_A, 'A')
    # print(count_B, 'B')

if A_num > B_num:
    order_A_in_C.append(count)
else:
    order_B_in_C.append(count)

print(*order_A_in_C)        
print(*order_B_in_C)