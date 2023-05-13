N = int(input())

S = list(input())

takahashi_win = 0
aoki_win = 0

for i in S:
    if i == "T":
        takahashi_win += 1
    elif i == "A":
        aoki_win += 1
    if takahashi_win == N // 2 and N %2 == 0:
        print("T")
        exit()
    elif aoki_win == N // 2 and N % 2 == 0:
        print("A")
        exit()

if takahashi_win > aoki_win:
    print("T")
else:
    print("A")
