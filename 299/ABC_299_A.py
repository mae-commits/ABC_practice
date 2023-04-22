N = int(input())

S = list(input())

between_judge = False

for letter in S:
    if letter == '|' and between_judge == False:
        between_judge = True
    elif letter == '*' and between_judge == True:
        print('in')
        exit()
    elif letter == '|' and between_judge == True:
        between_judge = False
        print('out')
        exit()