# 答えの組の保存
ans = []

def factorial(n):
    num = 1
    for i in range(n):
        num *= i+1
    return num

def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

for n in range(2,21):
    for k in range(1,n-1):
        left_cal = C(n+2, k+1)
        right_cal = 2 * (C(n, k-1) +  C(n, k+1))
        if left_cal == right_cal:
            ans.append([n,k])
    
for ans_combination in ans:
    print(*ans_combination)
