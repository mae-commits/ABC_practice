H, W = map(int,input().split())

squences_A = list(list(map(int,input().split())) for i in range(H))

ans_squences_A = []

for ith_line in squences_A:
    ith_letter_line = ""
    for num in ith_line:
        if num!=0:
            ith_letter_line+=(chr(num+64))
        else:
            ith_letter_line+=(".")
    ans_squences_A.append(ith_letter_line)

for letter_lines in ans_squences_A:
    print(letter_lines)