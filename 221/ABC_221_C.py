

N = list(input())

max_multiply = 0

for bit in range(1<<len(N)):
    number_a = ""
    number_b = ""
    for i in range(len(N)):
        if bit == 0 or bit == 1<<len(N) - 1:
            continue
        elif bit >> i & 1:
            number_a += N[i]
        else:
            number_b += N[i]
    if len(number_a) > 0 and len(number_b) > 0:
        a_list = list(number_a)
        b_list = list(number_b)
        a_list = sorted(map(int, a_list), reverse = True)
        b_list = sorted(map(int, b_list), reverse = True)
        max_a = int("".join(map(str, a_list)))
        max_b = int("".join(map(str, b_list)))
        max_multiply = max(max_a * max_b, max_multiply)
print(max_multiply)