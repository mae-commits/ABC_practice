# from collections import deque
# n = int(input())
# t_k = deque(list(map(int,input().split())) for i in range(n))
# need = [0 for i in range(n+1)]
# timeList = [0]

# for i in range(n):
#     t_k_i = t_k.popleft()
#     timeList.append(t_k_i[0])
#     need[i+1] = t_k_i[2:]

# 入力の受け取り
N=int(input())

# T,Aの受け取りリスト
T=[0]
A=[[0]]

# N回
for i in range(N):
    # リストで受け取り
    tmp=list(map(int,input().split()))
    # 0番目の要素がT
    T.append(tmp[0])
    # 1番目の要素がK
    K=tmp[1]
    # 0<Kならば
    if 0<K:
        # 2番目以降の要素がA
        a_list=tmp[2:]
        # Aに格納
        A.append(a_list)
    # そうでなければ(K=0)
    else:
        # ダミーとして-1を格納
        A.append([-1])

# キューを用意
from collections import deque
que=deque()

# 習得する必要がある技を管理
# Trueなら習得する
learn=[False]*(N+1)

# キューにNを追加
que.append(N)
# Nは習得する→learn[N]
learn[N]=True

# キューが空になるまで→キューの長さが0でなければ
while 0<len(que):
    # キューから取り出す
    waza=que.popleft()
    # wazaを学ぶために必要な技
    for x in A[waza]:
        # ダミーだったら
        if x==-1:
            # ループを抜ける
            break
        # まだ習得する技リストに入っていなければ
        # learn[x]がFalseならば
        if learn[x]==False:
            # キューに追加
            que.append(x)
            # learn[x]をTrueに
            learn[x]=True

# 答えの計算用
ans=0

# 1～Nまで
for i in range(1,N+1):
    # 習得する技なら
    if learn[i]==True:
        # T[i]時間かかる
        # 答えにT[i]を追加
        ans+=T[i]

# 答えを出力
print(ans)