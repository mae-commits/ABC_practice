from collections import deque

N = int(input()) # the number of people
S = input() # the strings of i th people
W = list(map(int,input().split())) # the sequences of the weights of all people
    
Adult = [] # the list of adults' tall.

Child = [] # the list of children's tall.

for i in range(N):
    if S[i] == "0":
        Child.append(W[i])
    else:
        Adult.append(W[i])

""" sort from small to high for children and adults."""
Child.sort()
Adult.sort()

ans = 0 # the number of people who can be correctly distinguished.

ans_old = 0 # it is used for reserving the number of ans.

# miss_judge_a = 0 # the number of adults who are incorrectly judged.

# miss_judge_c = 0 # the number of children who are incorrectly judged.

len_adult = len(Adult)

len_child = len(Child)

# judge from the tall of adults
k = 0
for i in range(len_adult):
    Y = Adult[i]
    while k <= len_child - 1 and Y > Child[k]:
            k += 1
    # len_adult - i: the number of adults who can be correctly judged. 
    # k: the number of children who can be correctly judged.
    ans_old = (len_adult -i) + k 
    ans = max(ans_old,ans)

""" sort from high to small for children and adults."""
Child.sort(reverse=True)
Adult.sort(reverse=True)

# judge from the tall of children
k = 0
for i in range(len_child):
    X = Child[i] + 0.1
    while k <= len_adult -1 and X <= Adult[k]:
            k += 1
    # len_child: the number of children who can be correctly judged.
    # k: the number of adults who can be correctly judged.
    ans_old = (len_child -i) + k
    ans = max(ans_old,ans)

print(ans)

