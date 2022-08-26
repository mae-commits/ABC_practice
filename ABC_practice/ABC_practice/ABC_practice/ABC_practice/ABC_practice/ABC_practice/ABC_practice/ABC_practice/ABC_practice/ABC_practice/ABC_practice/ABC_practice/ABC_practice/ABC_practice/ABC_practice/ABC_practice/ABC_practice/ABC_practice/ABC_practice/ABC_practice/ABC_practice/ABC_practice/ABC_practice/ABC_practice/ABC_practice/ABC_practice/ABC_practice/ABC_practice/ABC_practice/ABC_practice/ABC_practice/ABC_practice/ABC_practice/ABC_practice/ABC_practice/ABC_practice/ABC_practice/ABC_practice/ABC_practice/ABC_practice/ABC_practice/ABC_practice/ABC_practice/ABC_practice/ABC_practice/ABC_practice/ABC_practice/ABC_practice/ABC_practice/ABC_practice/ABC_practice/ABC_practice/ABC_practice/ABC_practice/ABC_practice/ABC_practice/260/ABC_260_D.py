from collections import deque

"""
N: the number of cards.
K: the condition of the number of cards which should be eaten.
"""
N, K = map(int,input().split())

"""
P: the initial order of cards from the top.
"""
P = deque(map(int,input().split()))

"""
turn: turn of being eaten for each number of card.
"""
turn = [-1]*N

"""
front: the deque type list of front cards.
"""
front = [[]]

"""
define whether the top value was added into the top of already existed cards.
def_top = -1: add the new colection.
def_top = 0: add the already exsiting collection.
"""
def_top = -1

for i in range(N):
    top = P.popleft()
    if len(front) >= 1:
        for j in range (len(front)):
            if front[j][0] > top:
                front[j] = [top] + front[j]
                if len(front[j]) == K:
                    for k in range (len(front[j])):
                        turn[front[j][k]-1] = i+1
                    front[j] = []
                    def_top = 0
                    break
    if def_top == -1 and K == 1:
        turn[top-1] = i+1
    elif def_top == -1 and K >= 2:
        front.append([top])
    front.sort()
    def_top = -1
    print(front)

for i in range(N):
    print(turn[i])