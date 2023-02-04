import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

p = [-1] * N
def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]
 
def merge(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  p[y] = x

count = 0
deg = [0] * N
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  deg[A] += 1
  deg[B] += 1
  if root(A) == root(B):
#     exit(print('No'))
    count += 1
  merge(A, B)
    
print(count)