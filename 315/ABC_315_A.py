import re

S = input()

S_ans = re.sub(r"[aiueo]", "", S)

print(S_ans)