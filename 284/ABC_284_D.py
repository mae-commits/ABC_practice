import math

# 素数のうち、小さい方の素数を判定
def judge(num):
    prime_numbers = [2]
    for i in range(3, int(pow(num, 1/3))):
        for j in range(int(math.sqrt(i))+1):
            if i%j == 0:
                break
            

# テストケースの数
T = int(input())

prime_numbers = []

for i in range(T):
    # 入力
    test = int(input())