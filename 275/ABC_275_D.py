from functools import lru_cache
@lru_cache(maxsize=1000)

def f(k):
    if k >= 1:
        return f(k//2) + f(k//3)
    else:
        return 1

n = int(input())
    
print(f(n))