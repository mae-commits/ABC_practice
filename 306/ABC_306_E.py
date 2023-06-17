import heapq

N, K, Q = map(int, input().split())
A = [0 for i in range(N)]

# K版間までで大きな数字の合計値
f_A = 0

# K番目までの数字の配列（キュー)
A_K_que = [0 for i in range(K)]
# K番目までに入っているインデックスを記憶
A_K_index = set(i+1 for i in range(K))

# 残りの分の配列
A_rest = [[0, i+1] for i in range(K)]

heapq.heapify(A_K_que)
heapq.heapify(A_rest)

for i in range(Q):
    X_i, Y_i = map(int, input().split())
    # 要素を変更する前の数字を記憶
    ex_A = A[X_i-1]
    #要素を変更
    A[X_i-1] = Y_i
    # K番目までの数字の中で最小値を出す
    A_K = heapq.heappop(A_K_que)
    # K+1 番目以降の数字の中で最大値を出す
    A_K_1 = heapq.heappop(A_rest)*(-1)
    
    # すでに該当のインデックスがK番目までの数字に含まれている場合
    if X_i in A_K_index:
        A_K_que.remove(ex_A)
        A_K_que.append(A_K)
        # 変更後がK番目以降になってしまう場合
        if Y_i < A_K_1[0]:
            A_K_que.append(A_K_1[0])
            A_K_index.add(A_K_1[1])
            A_rest.append([Y_i, X_i])
            f_A += (A_K_1[0] - ex_A)
        # そうでない場合
        else:
            A_K_que.append(Y_i)
            f_A += (Y_i - ex_A)
    # K+1番目以降の場合
    else:
        