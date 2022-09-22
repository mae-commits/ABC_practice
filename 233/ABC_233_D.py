# 入力の受け取り
N,K=map(int,input().split())
A=list(map(int,input().split()))

# Aの累積和
A_cum=[0]*(N+1)

# i=0~(N-1)まで
for i in range(N):
    # 累積和を計算
    A_cum[i+1]=A_cum[i]+A[i]

# defaultdictをインポート
from collections import defaultdict
# 連想配列
X=defaultdict(int)
# 答えをカウント
ans=0

# i=1~Nまで
for i in range(1,N+1):
    # A_cum[i-1]が増える
    X[A_cum[i-1]]+=1
    # A_cum[i]-Kとなるものをカウント
    ans+=X[A_cum[i]-K]

# Outpit answers
print(ans)