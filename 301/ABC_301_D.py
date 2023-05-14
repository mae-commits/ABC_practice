import math

S = list(input())

N = int(input())

# N をバイナリ変換
N_bin = list(map(str, format(N, 'b')))

# 整数Nを2進数表示した際の桁数をカウント
N_bin_digit = len(N_bin)

if N_bin_digit > len(S):
    S = ["0" for i in range(N_bin_digit-len(S))] + S
else:
    N_bin = ["0" for i in range(len(S)-N_bin_digit)] + N_bin

# 各2進数について1桁目からの順番で逆にソート
S.reverse()
N_bin.reverse()

S_new = S

print(S)
print(S_new)

# S, N それぞれについて各桁を比較
# '?' の場合は 'N' 似合うように変更
for i in range(len(S)):
    if S[i] == "?" and i >= N_bin_digit:
        S[i] = N_bin[i]
    elif S[i] == "?" and i < N_bin_digit:
        S[i] = "1"
    if S_new[i] == "?":
        S_new[i] = "0"
    
S.reverse()
S_new.reverse()

changed_S = int("".join(S), 2)
changed_S_new = int("".join(S_new), 2)

print(S)
print(S_new)

if N >= changed_S:
    print(changed_S)
elif changed_S_new <= N:
    print(changed_S_new)
else:
    print(-1)