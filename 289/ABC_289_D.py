
# ロボットが登ることのできる段数の種類の数

N = int(input())

# ロボットが上ることのできる段数

A = list(map(int, input().split()))

# 階段上のモチの個数

M = int(input())

# モチが存在する階段の番号

B = list(map(int, input().split()))

# ゴールの階段の番号

X = int(input())

# モチの存在判定

moti = [True] * (10**5+10)

for B_i in B:
    moti[B_i] = False

#  階段のある段に到達できるかどうかのDP

dp = [False] * (X+1)

dp[0] = True

# 始点の階段番号

for i in range(X):
    
    # 到達可能な段数であれば

    if dp[i] :
        for a in A:
            
            # モチが存在しない場合は到達可能

            if i + a <= X and moti[i + a]:
                dp[i+a] = True

# X段目が"True"の場合は "Yes"

if dp[-1]:
    print("Yes")

# そうでない場合は "No"

else:
    print("No")
    
    