import itertools

N, M = map(int, input().split())

# 文字列の入力
S = list(input() for i in range(N))

# 比較する数列番号の順列の取得
permutation_lists = list(itertools.permutations(range(N), N))

# 並び替えた文字列の保存
T = ["" for i in range(N)]
ans = "No"

for lists in permutation_lists:
    # 文字列の並び替え
    for i in range(N):
        T[i] = S[lists[i]]
        if i >= 1:
            dif = 0
            for j in range(M):
                if T[i][j] != T[i-1][j]:
                    dif += 1
            if dif != 1:
                break
        if i == N-1:
            print("Yes")
            exit()
            
print("No")