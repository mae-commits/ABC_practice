# 入力の受け取り
S=input()
# 「atcoder」をTに格納
T="atcoder"

# 1文字ずつリストへ展開
Slist=list(S)

# 答え
ans=0

# i=0~6
for i in range(7):
    # Tのi文字目がSlistの何番目か確認
    indx=Slist.index(T[i])

    # indxがiでない(正しい位置に来ていない)間
    while indx!=i:
        # indx番目と(indx-1)番目を入れ替え
        Slist[indx],Slist[indx-1]=Slist[indx-1],Slist[indx]
        # 次の文字へ
        indx-=1
        # 操作回数をカウント
        ans+=1

# 答えの出力
print(ans)