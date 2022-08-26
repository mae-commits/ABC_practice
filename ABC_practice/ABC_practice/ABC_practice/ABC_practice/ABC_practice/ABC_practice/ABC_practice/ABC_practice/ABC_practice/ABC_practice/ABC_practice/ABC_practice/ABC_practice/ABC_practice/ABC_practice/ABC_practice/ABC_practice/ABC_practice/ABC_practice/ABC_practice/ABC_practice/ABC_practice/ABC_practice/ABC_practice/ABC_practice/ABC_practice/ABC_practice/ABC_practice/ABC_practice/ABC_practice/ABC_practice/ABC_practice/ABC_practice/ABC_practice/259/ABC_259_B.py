import math

a,b,d = map(int,input().split())

# r = math.sqrt(a^2 + b^2)

a_new = a * math.cos(d/180 * math.pi) - b * math.sin(d/180 * math.pi)

b_new = a * math.sin(d/180 * math.pi) + b * math.cos(d/180 * math.pi)

print(str(a_new) + " " + str(b_new))