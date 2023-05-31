import math

# テストケースの数
T = int(input())


for i in range(T):
    # 入力
    test = int(input())
    for j in range(2, int(math.pow(test, 1/3))+1):
        if test % (j ** 2) == 0:
            print(j, test//(j ** 2))
            break
        elif test % j == 0:
            print(int(math.sqrt(test/j)), j)
            break