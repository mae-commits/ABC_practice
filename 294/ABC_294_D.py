from heapq import heapify, heappop, heappush

N, Q = list(map(int,input().split()))

# 呼ばれていない人の番号
# 今回は数字の小さい順に人が呼ばれていくので、
# 1のイベントが起こった際に番号を1ずつ加算
nex = 1

# 受付に呼ばれている人の番号
H = []

# 優先度つきキューにリストを変換
heapify(H)

# 受付に行った人の番号
wait = set()

for _ in range(Q):
    event = list(map(int,input().split()))
    # 1種類目のイベントならば、
    # 呼ばれていない最小の番号を呼ばれた人のリストに追加
    if event[0] == 1:
        heappush(H,nex)
        nex += 1
    # 2種類目のイベントならば、
    # 受付に行った人の番号のリストに追加
    elif event[0] == 2:
        x= event[1]
        wait.add(x)
    # 3種類目のイベント
    else:
        while H:
            # 受付に呼ばれた人のうち、最小の番号の人が
            # すでに受付に行っているかを調べる
            # 存在する場合は最小要素をpopする
            if H[0] in wait:
                heappop(H)
            # 存在しない場合は再度呼ぶので出力し、
            # ループを抜ける
            else:
                print(H[0])
                break