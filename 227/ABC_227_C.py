import math

n = int(input())
# nRange = int(math.pow(n,1/3))

count = 0

# for a in range(1,nRange + 1):
#     nRangeNew = int(math.pow(n//a, 1/2))
#     for b in range(a,nRangeNew+1):
#         cMax = n // (a * b)
#         count += cMax - b + 1


for a in range(1,n+1):
    if a * a * a >n:
        break
    else:
        for b in range(a,n+1):
            if a * b * b > n:
                break
            else:
                count += n//(a * b) - b + 1
                        
print(count)