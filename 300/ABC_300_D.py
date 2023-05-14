import math

# 素数 s を探す関数
def search_simple_number(num):
    simple_number = [2]
    for s in range(3, num):
        div_num = 0
        sqrt_s = int(math.sqrt(s))
        for div in range(2, sqrt_s + 1):
            if s % div == 0:
                div_num += 1
                break
        if div_num == 0:
            simple_number.append(s)
    return simple_number, len(simple_number)
        
N = int(input())

simple_number_list, length = search_simple_number(int((N)**0.5))

if length <= 2:
    print(0)
    exit()

ans = 0
    
for i in range(length-2):
    if simple_number_list[i] > int(math.ceil(N**0.2)):
        break
    for j in range(i+1, length-1):
        multi = simple_number_list[i] * simple_number_list[i] * simple_number_list[j]
        if multi > int(math.ceil(N**0.6)):
            break
        for k in range(j+1, length):
            if multi * simple_number_list[k] * simple_number_list[k] <= N:
                ans += 1
            else:
                break
print(ans)