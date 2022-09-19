# 入力の受け取り
N=int(input())

# 黒いマスの管理
Grid=[[0]*3000 for i in range(3000)]

# スタート地点の候補
Start=[]

# N回
for i in range(N):
    # 入力の受け取り
    X,Y=map(int,input().split())
    # 0以上にするため1000プラスする
    X+=1000
    Y+=1000
    # (X,Y)が黒いマス
    Grid[X][Y]=1
    # スタート地点の候補
    Start.append([X,Y])

# 訪問済み座標の管理
visited=[[False]*3000 for i in range(3000)]

# dequeを用意
from collections import deque
que=deque()

# 答え
ans=0

# (1)Startから座標を取り出す
for X,Y in Start:
    # (2)取り出した座標が訪問済みでなければキューに入れて、訪問済みにする
    if visited[X][Y]==0:
        # キューへ追加
        que.append([X,Y])
        # 訪問済みにする
        visited[X][Y]=1
        # 答えをプラス1
        ans+=1

        # (4)キューが空になるまで
        while 0<len(que):
            # 今いる座標
            NowX,NowY=que.popleft()

            # ・今いる場所(キューから取り出した座標)から進める座標が黒いマス かつ 訪問済みでなければ
            if Grid[NowX-1][NowY-1]==1 and visited[NowX-1][NowY-1]==0:
                # (4_1)訪問済みにする
                visited[NowX-1][NowY-1]=1
                # (4_2)座標をキューに入れる
                que.append([NowX-1,NowY-1])
            if Grid[NowX-1][NowY]==1 and visited[NowX-1][NowY]==0:
                visited[NowX-1][NowY]=1
                que.append([NowX-1,NowY])
            if Grid[NowX][NowY-1]==1 and visited[NowX][NowY-1]==0:
                visited[NowX][NowY-1]=1
                que.append([NowX,NowY-1])
            if Grid[NowX][NowY+1]==1 and visited[NowX][NowY+1]==0:
                visited[NowX][NowY+1]=1
                que.append([NowX,NowY+1])
            if Grid[NowX+1][NowY]==1 and visited[NowX+1][NowY]==0:
                visited[NowX+1][NowY]=1
                que.append([NowX+1,NowY])
            if Grid[NowX+1][NowY+1]==1 and visited[NowX+1][NowY+1]==0:
                visited[NowX+1][NowY+1]=1
                que.append([NowX+1,NowY+1])

# 答えの出力
print(ans)
