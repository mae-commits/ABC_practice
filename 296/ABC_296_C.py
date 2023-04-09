# 入力を受け取る
N, X = map(int, input().split())
A = list(map(int, input().split()))

# ハッシュテーブルを初期化する
hash_table = {}

# ハッシュテーブルに要素を格納する
for i in range(N):
    hash_table[A[i]+X] = i

# 数列 A の要素を順番に見ていき、ハッシュテーブルに要素が存在するか調べる
for i in range(N):
    if A[i] in hash_table:
        # 条件を満たす組が存在するため、Yes を出力して終了する
        print("Yes")
        exit()

# 条件を満たす組が存在しないため、No を出力する
print("No")
