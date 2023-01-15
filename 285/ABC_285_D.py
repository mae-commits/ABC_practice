from collections import deque

n = int(input())

s = []
t = []
username = set()
new_username = set()

for i in range(n):
    s_i,t_i = map(str,input().split())
    username.add(s_i)
    new_username.add(t_i)
    