from collections import defaultdict

S = input()

# "(" 囲み終わっていない部分の英小文字の記録
X = []

# a ~ z がすでに箱に入っているか管理
Y = defaultdict(int)

# 今見ている()の中身を管理
now = set()

for s in S:
    if s == '(':
        X.append(now)
        now = set()
        continue
    # () で閉じ終わったら、閉じられる部分の英小文字のボールを取り出す
    if s == ")":
        for t in now:
            Y[t] = 0
        # 取り出した英小文字を一気に記録から消去
        now = X.pop()
        continue
    # 英小文字のボールを追加する際に同じ文字の書かれたボールがないかを確認
    if Y[s] != 0:
        print("No")
        exit()
    # s を使用済みに変更
    Y[s] = 1
    
    # 今見ている () に s が存在することを記録
    now.add(s)

print("Yes")