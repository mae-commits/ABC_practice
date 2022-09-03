import sys

S = input()

if S[0] == "1":
    print("No")
    sys.exit()

first = [S[6]]

second = [S[3]]

third = [S[1],S[7]]

fourth = [S[4]]

fifth = [S[2],S[8]]

sixth = [S[5]]

seventh = [S[9]]

if first == ["1"] and second == ["0"] and ("1" in (third or fourth or fifth or sixth or seventh)):
    print("Yes")
    sys.exit()
if ("1" in first or "1" in second) and third == ["0","0"] and ("1" in fourth or "1" in fifth or "1" in sixth or "1" in seventh):
    print("Yes")
    sys.exit()
if ("1" in first or "1" in second or "1" in third) and fourth == ["0"] and ("1" in fifth or "1" in sixth or "1" in seventh):
    print("Yes")
    sys.exit()
if  ("1" in first or "1" in second or "1" in third or "1" in fourth) and fifth == ["0","0"] and ("1" in sixth or "1" in seventh):
    print("Yes")
    sys.exit()
if ("1" in first or "1" in second or "1" in third or "1" in fourth or "1" in fifth) and sixth == ["0"] and seventh == ["1"]:
    print("Yes")
    sys.exit()
print("No")