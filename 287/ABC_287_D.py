from collections import deque
import sys 

s=input()
t=input()

t_length=len(t)

s_head=""
s_tail=s[-t_length::]
s_list=deque(list(s))

for i in range(t_length+1):
    if i!=0:
        s_i=s_list.popleft()
        s_head+=s_i
        deque(list(s_tail)).popleft()
        s_tail="".join(list(s_tail))
    s_new=s_head+s_tail
    count=0
    # print(s_new,t)
    for j in range(t_length):
        s_new_j=deque(list(s_new)).popleft()
        t_j=deque(list(t)).popleft()
        if s_new_j!=t_j and (s_new_j!="?" and t_j!="?"):
            print("No")
            break
        else:
            count+=1
    if count==t_length:
        print("Yes")
        
        