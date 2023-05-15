S = list(reversed(input()))

N = int(input())

# 文字列Sのバイナリ変換の値
s = 0

# 文字列Sの中で`1`であるものだけバイナリ変換の値として加算
for i in range(len(S)):
    s |= (S[i] == "1") << i
# 表せる最小の値を超えてしまっている場合は-1
if s > N:
    print(-1)
# そうでない場合は、小さな桁から'?'を1に変換し、Nとの大小を比較
else:
    for i in reversed(range(len(S))):
        if S[i] == "?" and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)    