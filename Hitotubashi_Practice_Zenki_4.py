import sys

# x = 1 におけるf(1, n)の計算
def g(n):
    if n != 1:
        return g(n-1) + n
    else:
        return 1

# k = m + n
k = 2

while True:
    for m in range(1,k):
        n = k - m
        # 左辺の値を各々計算
        left_1st = g(m+n-1) - (m-1)
        left_2nd = g(m+n) - m
        left_3rd = g(m+n) - (m-1)
        left_4th = g(m+n+1) - m
        # 条件を満たす場合については、答えの組みを出力
        if left_1st + left_2nd + left_3rd + left_4th == 2023:
            print(m,n)
        # 左辺 > 4 * left_1st より、
        # それが2023を超えた場合はプログラムを終了
        if 4 * left_1st >= 2023:
            sys.exit()
    # ループを抜けた場合は次の直線上に移動
    k += 1