a, b = map(int,input().split())

s = round(float(b/a) * 1000) 

print('{:.3f}'.format(float(s/1000)))
