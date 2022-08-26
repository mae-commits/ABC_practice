A,B,C,D,E = map(int,input().split())

num_list = [A,B,C,D,E]

num_list.sort()

if (num_list[0] == num_list[1] and num_list[3] == num_list[4]) and (num_list[1] == num_list[2] or num_list[2] == num_list[3]):
    print("Yes")
else:
    print("No")