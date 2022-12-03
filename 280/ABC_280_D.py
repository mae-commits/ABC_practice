import math
from collections import deque
import sys

def prime_factorize(k):
    original_k = k
    i=1
    div=1
    while k%2==0:
        k//=2
        i+=1
    for num in range(1,int(math.sqrt(original_k))+1):
        i-=int(math.log(num*2,2))
        if i <= 0:
            div=num*2
            break
    f = 3
    while f*f<=k:
        j=1
        while k%f==0:
            k//=f
            j+=1
        for num in range(1,int(math.sqrt(original_k))+1):
            j-=int(math.log(num*f,f))
        if j <= 0:
            div=max(num*f,div)
            break
        f+=2
    if k!=1:
        return k
    else:
        return div

k = int(input())

print(prime_factorize(k))