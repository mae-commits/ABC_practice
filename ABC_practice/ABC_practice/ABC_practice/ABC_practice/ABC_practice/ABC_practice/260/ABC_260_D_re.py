from collections import defaultdict

class FenwickTree:
    def __init__(self,n):
        self._n=n
        self.data=[0]*n
    def add(self,p,x):
        p+=1
        while p<=self._n:
            self.data[p-1] +=x
            p+=p&-p
    def _sum(self,r):
        s=0
        while 0<r:
            s+=self.data[r-1]
            r-=r&-r
        return s
    def sum(self,l,r):
        r+=1
        return self._sum(r)-self._sum(l)
    def select(self,p):
        return self.sum(p,p)

Deck = defaultdict(list)

DeckNum = 0

N, K = map(int,input().split())

P = list(map(int,input().split()))

FT=FenwickTree(N+1)

CardDeck=[0]*(N+1)

ans=[-1]*(N+1)

def Nibutan(x):
    # (1)区間[左,右]を指定する
    # 左端=最小値(単調減少なら最大値)のインデックス番号
    # 右端=最大値(単調減少なら最小値)のインデックス番号
    l=x
    r=N

    # (4)1<(右-左)となっている間(2)~(4)を繰り返す
    while 1<r-l:
        # (2)中央=(左+右)//2が条件を満たすか確認
        c=(l+r)//2
        # FT[x]~FT[c]の区間和が1以上なら
        if 1<=FT.sum(x,c):
            # 右=中央と更新
            r=c
        # そうでなければ(FT[x]~FT[c]の区間和が0なら)
        else:
            # 左=中央と更新
            l=c

    # 右を返す
    return r

for i in range(N):
    # 引いたカード
    X=P[i]

    # K=1ならば
    if K==1:
        # カードXを(i+1)ターン目に食べることを記録
        ans[X]=i+1

    # FT[X]~FT[N]の区間和が0ならば
    # ⇔表に見えている中にXより大きい数字のカードはない
    elif FT.sum(X, N)==0:
        # 新しい山を作る
        # 山の番号をプラス1
        DeckNum+=1
        # DeckNum番目の山にXを追加
        Deck[DeckNum].append(X)
        # Xが場に見えている表向きのカードになる
        FT.add(X, 1)
        # XはDeckNum番目の山にあるカードであることを記録する
        CardDeck[X]=DeckNum

    # そうでなければ(FT[X]~FT[N]の区間和が1以上ならば)
    else:
        # p：場に見えている表向きのカードのうち、x以上で最小のもの
        p=Nibutan(X)
        # カードpが置かれている山の番号
        pNum=CardDeck[p]
        # カードXを山pNumに置く
        Deck[pNum].append(X)

        # カードpは場に見えている表向きのカードでなくなる
        FT.add(p, -1)
        # カードXが場に見えている表向きのカードになる
        FT.add(X, 1)
        # XはpNum番目の山にあるカードであることを記録する
        CardDeck[X]=pNum
    
        # pNum番目の山のカード枚数がK枚になったら
        # ⇔カードを食べる
        if len(Deck[pNum])==K:
            # q：pNum番目の山のカードそれぞれについて
            for q in Deck[pNum]:
                # (i+1)ターン目に食べたことを記録
                ans[q]=i+1
                
            # Xが表向きで場にあるカードでなくなる
            # ⇔マイナス1して0にする
            FT.add(X, -1)

# i=1~N
for i in range(1,N+1):
    # 答えの出力
    print(ans[i])
